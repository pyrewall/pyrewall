from pyrewall.core.db.database_session import DatabaseSession
from pyrewall.core.db.models.auth_source import AuthSource
from pyrewall.core.db.models.group import Group
from pyrewall.core.db.models.user import User

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
    pass

@di.inject
def setup_local_admin_user(db: DatabaseSession):
    user = db.session.query(User).filter(User.username == 'admin').one_or_none()
    if user is None:
        user = User()
        user.username = 'admin'
        user.enabled = True
        user.full_name = 'System Administrator'
        user.password = hashing_context.hash('pyrewall')
        user.unix_id = 10000

        user.created_by = user.id
        user.modified_by = user.id

        db.session.add(user)
        db.session.commit()

@di.inject
def setup_local_admin_user_group(db: DatabaseSession):
    pass

def seed_auth(dev: bool):
    setup_local_admin_user()
    setup_local_db_auth_source()
    setup_local_admin_group()
    