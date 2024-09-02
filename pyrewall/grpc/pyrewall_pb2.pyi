from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class voidNoArgs(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SystemInfoResponse(_message.Message):
    __slots__ = ("hostname",)
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    def __init__(self, hostname: _Optional[str] = ...) -> None: ...
