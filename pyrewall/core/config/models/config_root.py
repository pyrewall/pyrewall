from pydantic import BaseModel

from .system import System

class ConfigRoot(BaseModel):
    system: System