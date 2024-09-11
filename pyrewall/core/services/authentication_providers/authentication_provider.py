from abc import ABC, abstractmethod

class AuthenticationProvider(ABC):
    config: dict

    def __init__(self, config: dict) -> None:
        super().__init__()

        self.config = config

    @abstractmethod
    def authenticate_user_with_username_password(self, username: str, password: str) -> bool:
        raise NotImplementedError()