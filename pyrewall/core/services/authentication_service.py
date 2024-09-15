import logging

from abc import ABC, abstractmethod
from typing import Optional

from ..db.database_session import DatabaseSession
from ..db.models.auth_source import AuthSource
from ..dependency_injection import di

from ..models.authentication.authenticated_user import AuthenticatedUser
from ..models.authentication.token import Token
from ..models.user.user import User

from .authentication_provider_factory import AuthenticationProviderFactory
from .token_service import TokenService
from .user_service import UserService

_logging = logging.getLogger(__name__)

class AuthenticationService(ABC):
    def authenticate_user_with_username_password(self, username: str, password: str) -> Optional[AuthenticatedUser]:
        raise NotImplementedError()

class AuthenticationServiceImpl(AuthenticationService):
    _db: DatabaseSession
    _auth_provider_factory: AuthenticationProviderFactory
    _token_service: TokenService
    _user_service: UserService

    @di.inject
    def __init__(self, db: DatabaseSession, auth_provider_factory: AuthenticationProviderFactory, token_service: TokenService, user_service: UserService) -> None:
        super().__init__()

        self._db = db
        self._auth_provider_factory = auth_provider_factory
        self._token_service = token_service
        self._user_service = user_service

    def authenticate_user_with_username_password(self, username: str, password: str) -> AuthenticatedUser | None:
        providers = self._db.session.query(AuthSource).filter(AuthSource.enabled == True).order_by(AuthSource.priority.asc()).all()
        for provider in providers:
            auth_provider_type = self._auth_provider_factory.get_auth_provider(provider.type)
            auth_provider = auth_provider_type(provider.config)
            
            if auth_provider.authenticate_user_with_username_password(username, password):
                user = self._user_service.get_user_by_username(username)

                if user is None:
                    return None
                
                token = self._token_service.generate_token_for_user_id(user.id)

                return AuthenticatedUser(
                    user=user,
                    token=Token(
                        access_token=token,
                        expires_in=(60 * 60)
                    )
                )
        
        return None

di.register_scoped(AuthenticationService, AuthenticationServiceImpl)