from abc import ABC, abstractmethod
from typing import Optional

from ..db.database_session import DatabaseSession
from ..dependency_injection import di

from ..models.user.user import User

class AuthenticationService(ABC):
    def authenticate_user_with_username_password(self, username: str, password: str) -> Optional[User]:
        raise NotImplementedError()

class AuthenticationServiceImpl(AuthenticationService):
    _db: DatabaseSession

    @di.inject
    def __init__(self, db: DatabaseSession) -> None:
        super().__init__()

    def authenticate_user_with_username_password(self, username: str, password: str) -> User | None:
        return super().authenticate_user_with_username_password(username, password)

di.register_scoped(AuthenticationService, AuthenticationServiceImpl)