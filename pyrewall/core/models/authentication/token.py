from pydantic import BaseModel
from datetime import datetime

class Token(BaseModel):
    access_token: str
    expires_in: int
    expires_at: datetime