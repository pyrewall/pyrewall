from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    expires_in: int