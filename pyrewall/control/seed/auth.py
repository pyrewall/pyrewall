from pyrewall.core.db.database_session import DatabaseSession
from pyrewall.core.db.models.auth_source import AuthSource
from pyrewall.core.db.models.group import Group
from pyrewall.core.db.models.user import User
from pyrewall.core.db.models.user_groups import UserGroup

from pyrewall.core.dependency_injection import di

from pyrewall.utils.password import hashing_context

@di.inject
def get_admin_user(db: DatabaseSession) -> User:
    return db.session.query(User).filter(User.username == 'admin').one()

@di.inject
def setup_local_db_auth_source(db: DatabaseSession):
    admin_user: User = get_admin_user()
    auth_source = db.session.query(AuthSource).filter(AuthSource.name == 'Local Database', AuthSource.type == 'database').one_or_none()
    if auth_source is None:
        auth_source = AuthSource()
        auth_source.name = 'Local Database'
        auth_source.type = 'database'
        auth_source.enabled = True
        auth_source.created_by = admin_user.id
        auth_source.modified_by = admin_user.id
        auth_source.priority = 0
        db.session.add(auth_source)
        db.session.commit()

@di.inject
def setup_local_admin_group(db: DatabaseSession):
    group = db.session.query(Group).filter(Group.name == 'Super Admins').one_or_none()
    if group is None:
        admin_user: User = get_admin_user()
        group = Group()
        group.name = 'Super Admins'
        group.description = ''
        group.unix_id = 10_000
        group.permissions = ['*:*']
        group.created_by = admin_user.id
        group.modified_by = admin_user.id
        db.session.add(group)
        db.session.commit()


@di.inject
def setup_local_admin_user(db: DatabaseSession):
    user = db.session.query(User).filter(User.username == 'admin').one_or_none()
    if user is None:
        user = User()
        user.username = 'admin'
        user.enabled = True
        user.full_name = 'System Administrator'
        user.password = hashing_context.hash('pyrewall')
        user.unix_id = 10_000

        user.created_by = user.id
        user.modified_by = user.id

        db.session.add(user)
        db.session.commit()

@di.inject
def setup_local_admin_user_group(db: DatabaseSession):
    admin_user: User = get_admin_user()
    admin_group = db.session.query(Group).filter(Group.name == 'Super Admins').one()

    user_group = db.session.query(UserGroup).filter(UserGroup.user_id == admin_user.id, UserGroup.group_id == admin_group.id).one_or_none()
    if user_group is None:
        user_group = UserGroup()
        user_group.user_id = admin_user.id
        user_group.group_id = admin_group.id
        db.session.add(user_group)
        db.session.commit()


def seed_auth(dev: bool):
    setup_local_admin_user()
    setup_local_db_auth_source()
    setup_local_admin_group()
    setup_local_admin_user_group()
    