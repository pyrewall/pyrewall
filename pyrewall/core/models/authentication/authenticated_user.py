from pydantic import BaseModel

from ..user.user import User
from .token import Token

class AuthenticatedUser(BaseModel):
    user: User
    token: Token