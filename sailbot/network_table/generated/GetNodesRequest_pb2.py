# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetNodesRequest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='GetNodesRequest.proto',
  package='NetworkTable',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15GetNodesRequest.proto\x12\x0cNetworkTable\"\x1f\n\x0fGetNodesRequest\x12\x0c\n\x04uris\x18\x01 \x03(\tb\x06proto3')
)




_GETNODESREQUEST = _descriptor.Descriptor(
  name='GetNodesRequest',
  full_name='NetworkTable.GetNodesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uris', full_name='NetworkTable.GetNodesRequest.uris', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=70,
)

DESCRIPTOR.message_types_by_name['GetNodesRequest'] = _GETNODESREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetNodesRequest = _reflection.GeneratedProtocolMessageType('GetNodesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETNODESREQUEST,
  '__module__' : 'GetNodesRequest_pb2'
  # @@protoc_insertion_point(class_scope:NetworkTable.GetNodesRequest)
  })
_sym_db.RegisterMessage(GetNodesRequest)


# @@protoc_insertion_point(module_scope)
