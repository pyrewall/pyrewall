from pydantic import RootModel

from .user import User

class UserList(RootModel):
    root: list[User]