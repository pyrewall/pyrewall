from abc import ABC, abstractmethod

from ..dependency_injection import di

from .authentication_providers.authentication_provider import AuthenticationProvider

class AuthenticationProviderFactory(ABC):
    @abstractmethod
    def get_auth_provider(self, name: str) -> AuthenticationProvider:
        raise NotImplementedError()

class AuthenticationProviderFactoryImpl(AuthenticationProviderFactory):
    def get_auth_provider(self, name: str) -> AuthenticationProvider:
        return super().get_auth_provider(name)

di.register_scoped(AuthenticationProviderFactory, AuthenticationProviderFactoryImpl)