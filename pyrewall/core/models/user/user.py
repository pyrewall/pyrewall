from pydantic import BaseModel, Field
from uuid import UUID

class User(BaseModel):
    id: UUID
    