from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CreateUser(BaseModel):
    unix_id: Optional[int] = Field(None)
    username: str
    password: str
    enabled: bool
    full_name: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    expires: Optional[datetime] = Field(None)