# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: login_proto/login-grpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1clogin_proto/login-grpc.proto\x12\x0blogin_proto\x1a\x1bgoogle/protobuf/empty.proto\";\n\x15UserValidationRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"H\n\x16UserValidationResponse\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t2m\n\x10UserLoginService\x12Y\n\x0cValidateUser\x12\".login_proto.UserValidationRequest\x1a#.login_proto.UserValidationResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'login_proto.login_grpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USERVALIDATIONREQUEST']._serialized_start=74
  _globals['_USERVALIDATIONREQUEST']._serialized_end=133
  _globals['_USERVALIDATIONRESPONSE']._serialized_start=135
  _globals['_USERVALIDATIONRESPONSE']._serialized_end=207
  _globals['_USERLOGINSERVICE']._serialized_start=209
  _globals['_USERLOGINSERVICE']._serialized_end=318
# @@protoc_insertion_point(module_scope)
