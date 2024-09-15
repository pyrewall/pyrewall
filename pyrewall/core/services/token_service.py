import jwt
from abc import ABC, abstractmethod
from datetime import datetime, UTC, timedelta
from uuid import UUID

from ..config import PYREWALL_CONFIG_DIR
from ..dependency_injection import di

class TokenService(ABC):
    @abstractmethod
    def generate_token_for_user_id(self, user_id: UUID) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def validate_token(self, token: str) -> UUID:
        raise NotImplementedError()

class TokenServiceImpl(TokenService):
    def generate_token_for_user_id(self, user_id: UUID) -> str:
        payload = {
            "sub": str(user_id),
            "nbf": datetime.now(UTC),
            "iat": datetime.now(UTC),
            "exp": (datetime.now(UTC) + timedelta(minutes=60))
        }
        with open(f'{PYREWALL_CONFIG_DIR}private_key.pem', 'rb') as key_file:
            key = key_file.read()
        token = jwt.encode(payload, key, algorithm="RS256")
        return token
        
    def validate_token(self, token: str) -> UUID:
        with open(f'{PYREWALL_CONFIG_DIR}public_key.pem', 'rb') as key_file:
            key = key_file.read()
        payload = jwt.decode(token, key, algorithms=['RS256'])
        return UUID(payload['sub'])
        

di.register_singleton(TokenService, TokenServiceImpl)