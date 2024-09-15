from abc import ABC, abstractmethod

from ..dependency_injection import di

from .authentication_providers.authentication_provider import AuthenticationProvider

from .authentication_providers.database import DatabaseAuthenticationProvider

class AuthenticationProviderFactory(ABC):
    @abstractmethod
    def get_auth_provider(self, name: str) -> type[AuthenticationProvider]:
        raise NotImplementedError()

class AuthenticationProviderFactoryImpl(AuthenticationProviderFactory):
    def get_auth_provider(self, name: str) -> type[AuthenticationProvider]:
        match name:
            case 'database':
                return DatabaseAuthenticationProvider
            case _:
                raise NotImplementedError(name)

di.register_scoped(AuthenticationProviderFactory, AuthenticationProviderFactoryImpl)