# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bstate.proto\x12\x06protos\"s\n\x08Metadata\x12\x34\n\nproperties\x18\x01 \x03(\x0b\x32 .protos.Metadata.PropertiesEntry\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa7\x01\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x32\n\x08metadata\x18\x02 \x03(\x0b\x32 .protos.GetRequest.MetadataEntry\x12\'\n\x07options\x18\x03 \x01(\x0b\x32\x16.protos.GetStateOption\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"%\n\x0eGetStateOption\x12\x13\n\x0b\x63onsistency\x18\x01 \x01(\t\"\x8f\x01\n\x0bGetResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\x33\n\x08metadata\x18\x03 \x03(\x0b\x32!.protos.GetResponse.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc4\x01\n\nSetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0c\n\x04\x65tag\x18\x03 \x01(\t\x12\x32\n\x08metadata\x18\x04 \x03(\x0b\x32 .protos.SetRequest.MetadataEntry\x12\'\n\x07options\x18\x05 \x01(\x0b\x32\x16.protos.SetStateOption\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\":\n\x0eSetStateOption\x12\x13\n\x0b\x63oncurrency\x18\x01 \x01(\t\x12\x13\n\x0b\x63onsistency\x18\x02 \x01(\t\"\x07\n\x05\x45mpty\"\xbe\x01\n\rDeleteRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\x12\x35\n\x08metadata\x18\x03 \x03(\x0b\x32#.protos.DeleteRequest.MetadataEntry\x12*\n\x07options\x18\x04 \x01(\x0b\x32\x19.protos.DeleteStateOption\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"=\n\x11\x44\x65leteStateOption\x12\x13\n\x0b\x63oncurrency\x18\x01 \x01(\t\x12\x13\n\x0b\x63onsistency\x18\x02 \x01(\t2\xe0\x01\n\x05State\x12\'\n\x04Init\x12\x10.protos.Metadata\x1a\r.protos.Empty\x12.\n\x03Get\x12\x12.protos.GetRequest\x1a\x13.protos.GetResponse\x12(\n\x03Set\x12\x12.protos.SetRequest\x1a\r.protos.Empty\x12.\n\x06\x44\x65lete\x12\x15.protos.DeleteRequest\x1a\r.protos.Empty\x12$\n\x04Ping\x12\r.protos.Empty\x1a\r.protos.EmptyB)Z\'github.com/SSSOC-CAN/plugin_test/protosb\x06proto3')



_METADATA = DESCRIPTOR.message_types_by_name['Metadata']
_METADATA_PROPERTIESENTRY = _METADATA.nested_types_by_name['PropertiesEntry']
_GETREQUEST = DESCRIPTOR.message_types_by_name['GetRequest']
_GETREQUEST_METADATAENTRY = _GETREQUEST.nested_types_by_name['MetadataEntry']
_GETSTATEOPTION = DESCRIPTOR.message_types_by_name['GetStateOption']
_GETRESPONSE = DESCRIPTOR.message_types_by_name['GetResponse']
_GETRESPONSE_METADATAENTRY = _GETRESPONSE.nested_types_by_name['MetadataEntry']
_SETREQUEST = DESCRIPTOR.message_types_by_name['SetRequest']
_SETREQUEST_METADATAENTRY = _SETREQUEST.nested_types_by_name['MetadataEntry']
_SETSTATEOPTION = DESCRIPTOR.message_types_by_name['SetStateOption']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_DELETEREQUEST = DESCRIPTOR.message_types_by_name['DeleteRequest']
_DELETEREQUEST_METADATAENTRY = _DELETEREQUEST.nested_types_by_name['MetadataEntry']
_DELETESTATEOPTION = DESCRIPTOR.message_types_by_name['DeleteStateOption']
Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {

  'PropertiesEntry' : _reflection.GeneratedProtocolMessageType('PropertiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _METADATA_PROPERTIESENTRY,
    '__module__' : 'state_pb2'
    # @@protoc_insertion_point(class_scope:protos.Metadata.PropertiesEntry)
    })
  ,
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'state_pb2'
  # @@protoc_insertion_point(class_scope:protos.Metadata)
  })
_sym_db.RegisterMessage(Metadata)
_sym_db.RegisterMessage(Metadata.PropertiesEntry)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETREQUEST_METADATAENTRY,
    '__module__' : 'state_pb2'
    # @@protoc_insertion_point(class_scope:protos.GetRequest.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _GETREQUEST,
  '__module__' : 'state_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetRequest)
  })
_sym_db.RegisterMessage(GetRequest)
_sym_db.RegisterMessage(GetRequest.MetadataEntry)

GetStateOption = _reflection.GeneratedProtocolMessageType('GetStateOption', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATEOPTION,
  '__module__' : 'state_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetStateOption)
  })
_sym_db.RegisterMessage(GetStateOption)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETRESPONSE_METADATAENTRY,
    '__module__' : 'state_pb2'
    # @@protoc_insertion_point(class_scope:protos.GetResponse.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _GETRESPONSE,
  '__module__' : 'state_pb2'
  # @@protoc_insertion_point(class_scope:protos.GetResponse)
  })
_sym_db.RegisterMessage(GetResponse)
_sym_db.RegisterMessage(GetResponse.MetadataEntry)

SetRequest = _reflection.GeneratedProtocolMessageType('SetRequest', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _SETREQUEST_METADATAENTRY,
    '__module__' : 'state_pb2'
    # @@protoc_insertion_point(class_scope:protos.SetRequest.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _SETREQUEST,
  '__module__' : 'state_pb2'
  # @@protoc_insertion_point(class_scope:protos.SetRequest)
  })
_sym_db.RegisterMessage(SetRequest)
_sym_db.RegisterMessage(SetRequest.MetadataEntry)

SetStateOption = _reflection.GeneratedProtocolMessageType('SetStateOption', (_message.Message,), {
  'DESCRIPTOR' : _SETSTATEOPTION,
  '__module__' : 'state_pb2'
  # @@protoc_insertion_point(class_scope:protos.SetStateOption)
  })
_sym_db.RegisterMessage(SetStateOption)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'state_pb2'
  # @@protoc_insertion_point(class_scope:protos.Empty)
  })
_sym_db.RegisterMessage(Empty)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _DELETEREQUEST_METADATAENTRY,
    '__module__' : 'state_pb2'
    # @@protoc_insertion_point(class_scope:protos.DeleteRequest.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'state_pb2'
  # @@protoc_insertion_point(class_scope:protos.DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)
_sym_db.RegisterMessage(DeleteRequest.MetadataEntry)

DeleteStateOption = _reflection.GeneratedProtocolMessageType('DeleteStateOption', (_message.Message,), {
  'DESCRIPTOR' : _DELETESTATEOPTION,
  '__module__' : 'state_pb2'
  # @@protoc_insertion_point(class_scope:protos.DeleteStateOption)
  })
_sym_db.RegisterMessage(DeleteStateOption)

_STATE = DESCRIPTOR.services_by_name['State']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\'github.com/SSSOC-CAN/plugin_test/protos'
  _METADATA_PROPERTIESENTRY._options = None
  _METADATA_PROPERTIESENTRY._serialized_options = b'8\001'
  _GETREQUEST_METADATAENTRY._options = None
  _GETREQUEST_METADATAENTRY._serialized_options = b'8\001'
  _GETRESPONSE_METADATAENTRY._options = None
  _GETRESPONSE_METADATAENTRY._serialized_options = b'8\001'
  _SETREQUEST_METADATAENTRY._options = None
  _SETREQUEST_METADATAENTRY._serialized_options = b'8\001'
  _DELETEREQUEST_METADATAENTRY._options = None
  _DELETEREQUEST_METADATAENTRY._serialized_options = b'8\001'
  _METADATA._serialized_start=23
  _METADATA._serialized_end=138
  _METADATA_PROPERTIESENTRY._serialized_start=89
  _METADATA_PROPERTIESENTRY._serialized_end=138
  _GETREQUEST._serialized_start=141
  _GETREQUEST._serialized_end=308
  _GETREQUEST_METADATAENTRY._serialized_start=261
  _GETREQUEST_METADATAENTRY._serialized_end=308
  _GETSTATEOPTION._serialized_start=310
  _GETSTATEOPTION._serialized_end=347
  _GETRESPONSE._serialized_start=350
  _GETRESPONSE._serialized_end=493
  _GETRESPONSE_METADATAENTRY._serialized_start=261
  _GETRESPONSE_METADATAENTRY._serialized_end=308
  _SETREQUEST._serialized_start=496
  _SETREQUEST._serialized_end=692
  _SETREQUEST_METADATAENTRY._serialized_start=261
  _SETREQUEST_METADATAENTRY._serialized_end=308
  _SETSTATEOPTION._serialized_start=694
  _SETSTATEOPTION._serialized_end=752
  _EMPTY._serialized_start=754
  _EMPTY._serialized_end=761
  _DELETEREQUEST._serialized_start=764
  _DELETEREQUEST._serialized_end=954
  _DELETEREQUEST_METADATAENTRY._serialized_start=261
  _DELETEREQUEST_METADATAENTRY._serialized_end=308
  _DELETESTATEOPTION._serialized_start=956
  _DELETESTATEOPTION._serialized_end=1017
  _STATE._serialized_start=1020
  _STATE._serialized_end=1244
# @@protoc_insertion_point(module_scope)