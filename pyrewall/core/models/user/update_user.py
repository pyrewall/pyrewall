from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class UpdateUser(BaseModel):
    password: Optional[str] = Field(None)
    enabled: Optional[bool] = Field(None)
    full_name: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    expires: Optional[datetime] = Field(None)