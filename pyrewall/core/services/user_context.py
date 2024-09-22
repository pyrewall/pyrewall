from abc import ABC, abstractmethod

from uuid import UUID

from ..db.database_session import DatabaseSession
from ..db.models.user import User as DBUser

class UserContext(ABC):
    _db: DatabaseSession

    _cached_user: DBUser

    def __init__(self, db: DatabaseSession) -> None:
        super().__init__()

        self._db = db

        self._cached_user = None

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

