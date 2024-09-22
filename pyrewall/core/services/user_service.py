from abc import ABC, abstractmethod
from uuid import UUID

from ..db.database_session import DatabaseSession
from ..db.models.user import User as DBUser
from ..dependency_injection import di

from ..models.user.user import User

class UserService(ABC):
    @abstractmethod
    def get_users(self) -> list[User]:
        raise NotImplementedError()
    
    @abstractmethod
    def get_user_by_id(self, user_id: UUID) -> User | None:
        raise NotImplementedError()
    
    @abstractmethod
    def get_user_by_unix_id(self, unix_user_id: int) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    def get_user_by_username(self, username: str) -> User | None:
        raise NotImplementedError()

class UserServiceImpl(UserService):
    _db: DatabaseSession

    @di.inject
    def __init__(self, db: DatabaseSession) -> None:
        super().__init__()

        self._db = db

    def _db_to_model(self, db_user: DBUser) -> User | None:
        if db_user is None:
            return None
        
        user = User(
            id=db_user.id,
            unix_id=db_user.unix_id,
            username=db_user.username,
            enabled=db_user.enabled,
            full_name=db_user.full_name,
            email=db_user.email,
            expires=db_user.expires,
            created_by_id=db_user.modified_by,
            created_date=db_user.created_date,
            created_by_user=None,
            modified_by_id=db_user.modified_by,
            modified_date=db_user.modified_date,
            modified_by_user=None
        )

        return user

    def get_users(self) -> list[User]:
        users = self._db.session.query(DBUser).all()

        return list(map(self._db_to_model, users))

    def get_user_by_id(self, user_id: UUID) -> User | None:
        user = self._db.session.query(DBUser).filter(DBUser.id == user_id).one_or_none()

        return self._db_to_model(user)

    def get_user_by_unix_id(self, unix_user_id: int) -> User | None:
        user = self._db.session.query(DBUser).filter(DBUser.unix_id == unix_user_id).one_or_none()

        return self._db_to_model(user)

    def get_user_by_username(self, username: str) -> User | None:
        user = self._db.session.query(DBUser).filter(DBUser.username == username).one_or_none()
        
        return self._db_to_model(user)    

di.register_scoped(UserService, UserServiceImpl)