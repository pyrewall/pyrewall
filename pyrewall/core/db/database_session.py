import logging
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from .engine import engine

from ..dependency_injection import di

_logger = logging.getLogger(__name__)

class DatabaseSession(ABC):
    @property
    @abstractmethod
    def session(self) -> Session:
        raise NotImplementedError()

class DatabaseSessionImpl(DatabaseSession):
    _session: Session

    def __init__(self) -> None:
        self._session = None
    
    def __del__(self):
        if self._session is not None:
            _logger.debug('Closing DB Session')
            self._session.close()
    
    @property
    def session(self) -> Session:
        if self._session is None:
            _logger.debug('Opening DB Session')
            self._session = Session(engine)
        return self._session

di.register_scoped(DatabaseSession, DatabaseSessionImpl)