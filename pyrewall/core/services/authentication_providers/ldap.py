from ldap3 import Server, Connection, SIMPLE, SYNC, ALL

from .authentication_provider import AuthenticationProvider

class LdapAuthenticationProvider(AuthenticationProvider):

    def __init__(self, config: dict) -> None:
        super().__init__(config)

    def authenticate_user_with_username_password(self, username: str, password: str) -> bool:
        s = Server()
        c = Connection(s, user=username, password=password)
        super().authenticate_user_with_username_password(username, password)