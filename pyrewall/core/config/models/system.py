from pydantic import BaseModel, Field
from uuid import UUID

from .user import User

class System(BaseModel):
    host_name: str = Field('pyrewall')
    instance_id: UUID = Field(UUID(int=0))
    users: list[User] = Field(default_factory=lambda: [])
