from sqlalchemy import or_, func
from pyrewall.utils.password import hashing_context

from ...db.database_session import DatabaseSession
from ...dependency_injection import di

from ...db.models.user import User as DBUser

from .authentication_provider import AuthenticationProvider

class DatabaseAuthenticationProvider(AuthenticationProvider):
    _db: DatabaseSession

    @di.inject
    def __init__(self, config: dict, db: DatabaseSession) -> None:
        super().__init__(config)

        self._db = db

    def authenticate_user_with_username_password(self, username: str, password: str) -> bool:
        user = self._db.session.query(DBUser).filter(DBUser.enabled == True, DBUser.username == username, DBUser.password != None, or_(DBUser.expires == None, DBUser.expires > func.current_timestamp())).one_or_none()

        if user is None:
            return False
        
        verified, new_hash = hashing_context.verify_and_update(password, user.password)
        
        if not verified:
            return False
        
        if new_hash is not None:
            user.password = new_hash
            self._db.session.commit()
        
        return True
