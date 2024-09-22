import logging
import jwt

from flask import request
from uuid import UUID

from werkzeug.exceptions import Unauthorized, Forbidden

from pyrewall.core.db.database_session import DatabaseSession
from pyrewall.core.dependency_injection import di
from pyrewall.core.services.token_service import TokenService
from pyrewall.core.services.user_context import UserContext

_logger = logging.getLogger(__name__)

class ApiUserContext(UserContext):
    _token_service: TokenService

    _user_id: UUID | None

    @di.inject
    def __init__(self, token_service: TokenService, db: DatabaseSession) -> None:
        super().__init__(db)

        self._token_service = token_service

    def setup_context(self, require_auth: bool = True):
        has_auth_header = 'Authorization' in request.headers
        if not has_auth_header and not require_auth:
            _logger.debug('Skipping auth')
            return
        
        if not has_auth_header and require_auth:
            raise Forbidden('Missing Authorization Token')
        
        try:
            auth_token = request.authorization.token
            self._user_id = self._token_service.validate_token(auth_token)
        except Exception as exc:
            _logger.exception(exc)
            if require_auth:
                raise Unauthorized() from exc
        
        if self.user is None and require_auth:
            raise Unauthorized()
    
    @property
    def user_id(self) -> UUID:
        return self._user_id
    
di.register_scoped(UserContext, ApiUserContext)