from pydantic import BaseModel
from datetime import datetime, UTC
from uuid import UUID
from pyrewall.core.permissions.permssion import Permission

def json_default(obj):
    if hasattr(obj, 'to_json'):
        return obj.to_json()
    if isinstance(obj, BaseModel):
        return obj.model_dump(by_alias=True)
    if isinstance(obj, datetime):
        return obj.replace(tzinfo=UTC).isoformat()
    if isinstance(obj, UUID):
        return str(obj)
    if isinstance(obj, Permission):
        return str(obj)
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')