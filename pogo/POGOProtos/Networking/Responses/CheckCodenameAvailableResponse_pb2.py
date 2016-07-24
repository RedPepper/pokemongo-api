# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Responses/CheckCodenameAvailableResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Responses/CheckCodenameAvailableResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\nDPOGOProtos/Networking/Responses/CheckCodenameAvailableResponse.proto\x12\x1fPOGOProtos.Networking.Responses\"\xc2\x02\n\x1e\x43heckCodenameAvailableResponse\x12\x10\n\x08\x63odename\x18\x01 \x01(\t\x12\x14\n\x0cuser_message\x18\x02 \x01(\t\x12\x15\n\ris_assignable\x18\x03 \x01(\x08\x12V\n\x06status\x18\x04 \x01(\x0e\x32\x46.POGOProtos.Networking.Responses.CheckCodenameAvailableResponse.Status\"\x88\x01\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1a\n\x16\x43ODENAME_NOT_AVAILABLE\x10\x02\x12\x16\n\x12\x43ODENAME_NOT_VALID\x10\x03\x12\x11\n\rCURRENT_OWNER\x10\x04\x12\x1f\n\x1b\x43ODENAME_CHANGE_NOT_ALLOWED\x10\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CHECKCODENAMEAVAILABLERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='POGOProtos.Networking.Responses.CheckCodenameAvailableResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CODENAME_NOT_AVAILABLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CODENAME_NOT_VALID', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CURRENT_OWNER', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CODENAME_CHANGE_NOT_ALLOWED', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=292,
  serialized_end=428,
)
_sym_db.RegisterEnumDescriptor(_CHECKCODENAMEAVAILABLERESPONSE_STATUS)


_CHECKCODENAMEAVAILABLERESPONSE = _descriptor.Descriptor(
  name='CheckCodenameAvailableResponse',
  full_name='POGOProtos.Networking.Responses.CheckCodenameAvailableResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='codename', full_name='POGOProtos.Networking.Responses.CheckCodenameAvailableResponse.codename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_message', full_name='POGOProtos.Networking.Responses.CheckCodenameAvailableResponse.user_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_assignable', full_name='POGOProtos.Networking.Responses.CheckCodenameAvailableResponse.is_assignable', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='POGOProtos.Networking.Responses.CheckCodenameAvailableResponse.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHECKCODENAMEAVAILABLERESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=428,
)

_CHECKCODENAMEAVAILABLERESPONSE.fields_by_name['status'].enum_type = _CHECKCODENAMEAVAILABLERESPONSE_STATUS
_CHECKCODENAMEAVAILABLERESPONSE_STATUS.containing_type = _CHECKCODENAMEAVAILABLERESPONSE
DESCRIPTOR.message_types_by_name['CheckCodenameAvailableResponse'] = _CHECKCODENAMEAVAILABLERESPONSE

CheckCodenameAvailableResponse = _reflection.GeneratedProtocolMessageType('CheckCodenameAvailableResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHECKCODENAMEAVAILABLERESPONSE,
  __module__ = 'POGOProtos.Networking.Responses.CheckCodenameAvailableResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.CheckCodenameAvailableResponse)
  ))
_sym_db.RegisterMessage(CheckCodenameAvailableResponse)


# @@protoc_insertion_point(module_scope)