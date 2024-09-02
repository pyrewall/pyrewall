
from .authentication_provider import AuthenticationProvider

class LdapAuthenticationProvider(AuthenticationProvider):

    def __init__(self, config: dict) -> None:
        super().__init__(config)

    def authenticate_user_with_username_password(self, username: str, password: str) -> bool:
        super().authenticate_user_with_username_password(username, password)