from abc import ABC, abstractmethod
from itertools import chain
from uuid import UUID

from ..db.database_session import DatabaseSession
from ..db.models.user import User as DBUser
from ..db.models.group import Group as DBGroup
from ..db.models.user_groups import UserGroup

from ..permissions.permssion import Permission

class UserContext(ABC):
    _db: DatabaseSession

    _cached_user: DBUser
    _cached_groups: list[DBGroup]
    _cached_permissions: list[Permission]

    def __init__(self, db: DatabaseSession) -> None:
        super().__init__()

        self._db = db

        self._cached_user = None
        self._cached_groups = None
        self._cached_permissions = None

    @abstractmethod
    def setup_context(self, require_auth: bool = True):
        raise NotImplementedError()
    
    @property
    @abstractmethod
    def user_id(self) -> UUID:
        raise NotImplementedError()
    
    @property
    def user(self) -> DBUser | None:
        if self._cached_user is None:
            self._cached_user = self._db.session.query(DBUser).filter(DBUser.id == self.user_id).one_or_none()
        return self._cached_user
    
    @property
    def groups(self) -> list[DBGroup]:
        if self._cached_groups is None:
            self._cached_groups = self._db.session.query(DBGroup).join(UserGroup, UserGroup.group_id == DBGroup.id).filter(UserGroup.user_id == self.user_id).all()
        return self._cached_groups
    
    @property
    def permissions(self) -> list[Permission]:
        if self._cached_permissions is None:
            self._cached_permissions = list(map(Permission.from_str, set(chain(*[g.permissions for g in self.groups]))))
        return self._cached_permissions


