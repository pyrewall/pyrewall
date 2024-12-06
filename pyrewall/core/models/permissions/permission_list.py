from pydantic import RootModel

from .permission import Permission

class PermissionList(RootModel):
    root: list[Permission]