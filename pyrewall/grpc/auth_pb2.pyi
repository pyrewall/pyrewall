from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class voidNoArgs(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class User(_message.Message):
    __slots__ = ("unixid", "username", "fullname", "shell")
    UNIXID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    FULLNAME_FIELD_NUMBER: _ClassVar[int]
    SHELL_FIELD_NUMBER: _ClassVar[int]
    unixid: int
    username: str
    fullname: str
    shell: str
    def __init__(self, unixid: _Optional[int] = ..., username: _Optional[str] = ..., fullname: _Optional[str] = ..., shell: _Optional[str] = ...) -> None: ...

class AllUsersResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...
