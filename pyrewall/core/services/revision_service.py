from abc import ABC, abstractmethod

from ..db.database_session import DatabaseSession
from ..db.models.revision import Revision as DBRevision
from ..dependency_injection import di
from ..models.revisions.revision import Revision

class RevisionService(ABC):
    def getRevision(self, id: int) -> Revision:
        raise NotImplementedError()
    
    def getActiveRevision(self) -> Revision:
        raise NotImplementedError()

    def getOpenRevision(self) -> Revision:
        raise NotImplementedError()
    
    def createRevision(self) -> Revision:
        raise NotImplementedError()

class RevisionServiceImpl(RevisionService):
    _db: DatabaseSession
    
    @di.inject
    def __init__(self, db: DatabaseSession):
        super().__init__()

        self._db = db

    def _revison_db_to_model(self, revision: DBRevision) -> Revision:
        if revision is None:
            return None
        
        raise NotImplementedError()

    def getRevision(self, id):
        revision = self._db.session.query(DBRevision).filter(DBRevision.id == id).one_or_none()

        return self._revison_db_to_model(revision)

    def getActiveRevision(self):
        revision = self._db.session.query(DBRevision).filter(DBRevision.applied_date != None).order_by(DBRevision.applied_date.desc()).limit(1).one_or_none()

        return self._revison_db_to_model(revision)
    
    def getOpenRevision(self):
        revision = self._db.session.query(DBRevision).filter(DBRevision.applied_date == None).order_by(DBRevision.created_date.desc()).limit(1).one_or_none()

        return self._revison_db_to_model(revision)
    
    def createRevision(self):
        return super().createRevision()

di.register_scoped(RevisionService, RevisionServiceImpl)