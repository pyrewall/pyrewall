from abc import ABC, abstractmethod

from ..db.database_session import DatabaseSession
from ..dependency_injection import di

from ..models.user.user import User

class UserService(ABC):
    @abstractmethod
    def get_user_by_username(self, username: str) -> User | None:
        raise NotImplementedError()

class UserServiceImpl(UserService):
    _db: DatabaseSession

    @di.inject
    def __init__(self, db: DatabaseSession) -> None:
        super().__init__()

        self._db = db

    def get_user_by_username(self, username: str) -> User | None:
        return super().get_user_by_username(username)
    

di.register_scoped(UserService, UserServiceImpl)