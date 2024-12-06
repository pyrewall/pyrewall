from pydantic import BaseModel

class Permission(BaseModel):
    permission: str
    entity: str
    action: str
    title: str
    description: str