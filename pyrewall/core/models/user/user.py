from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

class User(BaseModel):
    id: UUID
    unix_id: int
    username: str
    enabled: bool
    full_name: Optional[str]
    email: Optional[str]
    expires: Optional[datetime]
    
    created_date: datetime
    created_by_id: UUID
    # created_by_user: Optional["User"]

    modified_date: datetime
    modified_by_id: UUID
    # modified_by_user: Optional["User"]