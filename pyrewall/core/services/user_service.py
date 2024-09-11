from abc import ABC, abstractmethod

from ..db.database_session import DatabaseSession
from ..dependency_injection import di

class UserService(ABC):
    pass

class UserServiceImpl(UserService):
    _db: DatabaseSession

    @di.inject
    def __init__(self, db: DatabaseSession) -> None:
        super().__init__()

        self._db = db
    

di.register_scoped(UserService, UserServiceImpl)