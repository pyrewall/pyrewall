# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: auth.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'auth.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\rpyrewall.auth\"\x0c\n\nvoidNoArgs\"I\n\x04User\x12\x0e\n\x06unixid\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08\x66ullname\x18\x03 \x01(\t\x12\r\n\x05shell\x18\x04 \x01(\t\"6\n\x10\x41llUsersResponse\x12\"\n\x05users\x18\x01 \x03(\x0b\x32\x13.pyrewall.auth.User2Y\n\x0cUsersService\x12I\n\x0bGetAllUsers\x12\x19.pyrewall.auth.voidNoArgs\x1a\x1f.pyrewall.auth.AllUsersResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_VOIDNOARGS']._serialized_start=29
  _globals['_VOIDNOARGS']._serialized_end=41
  _globals['_USER']._serialized_start=43
  _globals['_USER']._serialized_end=116
  _globals['_ALLUSERSRESPONSE']._serialized_start=118
  _globals['_ALLUSERSRESPONSE']._serialized_end=172
  _globals['_USERSSERVICE']._serialized_start=174
  _globals['_USERSSERVICE']._serialized_end=263
# @@protoc_insertion_point(module_scope)
