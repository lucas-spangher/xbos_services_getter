# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: indoor_data_historical.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='indoor_data_historical.proto',
  package='indoor_data_historical',
  syntax='proto3',
  serialized_options=_b('P\001'),
  serialized_pb=_b('\n\x1cindoor_data_historical.proto\x12\x16indoor_data_historical\"j\n\x07Request\x12\x10\n\x08\x62uilding\x18\x01 \x01(\t\x12\x0c\n\x04zone\x18\x02 \x01(\t\x12\r\n\x05start\x18\x03 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x04 \x01(\x03\x12\x0e\n\x06window\x18\x05 \x01(\t\x12\x13\n\x0b\x61ggregation\x18\x06 \x01(\t\"Y\n\x08Setpoint\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x17\n\x0ftemperature_low\x18\x02 \x01(\x01\x12\x18\n\x10temperature_high\x18\x03 \x01(\x01\x12\x0c\n\x04unit\x18\x04 \x01(\t\"C\n\x10TemperaturePoint\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x13\n\x0btemperature\x18\x02 \x01(\x01\x12\x0c\n\x04unit\x18\x03 \x01(\t\"+\n\x0b\x41\x63tionPoint\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\x01\"U\n\x13RawTemperatureReply\x12>\n\x0ctemperatures\x18\x01 \x03(\x0b\x32(.indoor_data_historical.TemperaturePoint\"F\n\x0eRawActionReply\x12\x34\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32#.indoor_data_historical.ActionPoint\"O\n\x18RawTemperatureBandsReply\x12\x33\n\tsetpoints\x18\x01 \x03(\x0b\x32 .indoor_data_historical.Setpoint2\xc7\x02\n\x14IndoorDataHistorical\x12\x64\n\x12GetRawTemperatures\x12\x1f.indoor_data_historical.Request\x1a+.indoor_data_historical.RawTemperatureReply\"\x00\x12Z\n\rGetRawActions\x12\x1f.indoor_data_historical.Request\x1a&.indoor_data_historical.RawActionReply\"\x00\x12m\n\x16GetRawTemperatureBands\x12\x1f.indoor_data_historical.Request\x1a\x30.indoor_data_historical.RawTemperatureBandsReply\"\x00\x42\x02P\x01\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='indoor_data_historical.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='building', full_name='indoor_data_historical.Request.building', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone', full_name='indoor_data_historical.Request.zone', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='indoor_data_historical.Request.start', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='indoor_data_historical.Request.end', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window', full_name='indoor_data_historical.Request.window', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aggregation', full_name='indoor_data_historical.Request.aggregation', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=56,
  serialized_end=162,
)


_SETPOINT = _descriptor.Descriptor(
  name='Setpoint',
  full_name='indoor_data_historical.Setpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='indoor_data_historical.Setpoint.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature_low', full_name='indoor_data_historical.Setpoint.temperature_low', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature_high', full_name='indoor_data_historical.Setpoint.temperature_high', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='indoor_data_historical.Setpoint.unit', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=164,
  serialized_end=253,
)


_TEMPERATUREPOINT = _descriptor.Descriptor(
  name='TemperaturePoint',
  full_name='indoor_data_historical.TemperaturePoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='indoor_data_historical.TemperaturePoint.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='indoor_data_historical.TemperaturePoint.temperature', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='indoor_data_historical.TemperaturePoint.unit', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=255,
  serialized_end=322,
)


_ACTIONPOINT = _descriptor.Descriptor(
  name='ActionPoint',
  full_name='indoor_data_historical.ActionPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='indoor_data_historical.ActionPoint.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='indoor_data_historical.ActionPoint.action', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=324,
  serialized_end=367,
)


_RAWTEMPERATUREREPLY = _descriptor.Descriptor(
  name='RawTemperatureReply',
  full_name='indoor_data_historical.RawTemperatureReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='temperatures', full_name='indoor_data_historical.RawTemperatureReply.temperatures', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=369,
  serialized_end=454,
)


_RAWACTIONREPLY = _descriptor.Descriptor(
  name='RawActionReply',
  full_name='indoor_data_historical.RawActionReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actions', full_name='indoor_data_historical.RawActionReply.actions', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=456,
  serialized_end=526,
)


_RAWTEMPERATUREBANDSREPLY = _descriptor.Descriptor(
  name='RawTemperatureBandsReply',
  full_name='indoor_data_historical.RawTemperatureBandsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='setpoints', full_name='indoor_data_historical.RawTemperatureBandsReply.setpoints', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=528,
  serialized_end=607,
)

_RAWTEMPERATUREREPLY.fields_by_name['temperatures'].message_type = _TEMPERATUREPOINT
_RAWACTIONREPLY.fields_by_name['actions'].message_type = _ACTIONPOINT
_RAWTEMPERATUREBANDSREPLY.fields_by_name['setpoints'].message_type = _SETPOINT
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Setpoint'] = _SETPOINT
DESCRIPTOR.message_types_by_name['TemperaturePoint'] = _TEMPERATUREPOINT
DESCRIPTOR.message_types_by_name['ActionPoint'] = _ACTIONPOINT
DESCRIPTOR.message_types_by_name['RawTemperatureReply'] = _RAWTEMPERATUREREPLY
DESCRIPTOR.message_types_by_name['RawActionReply'] = _RAWACTIONREPLY
DESCRIPTOR.message_types_by_name['RawTemperatureBandsReply'] = _RAWTEMPERATUREBANDSREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'indoor_data_historical_pb2'
  # @@protoc_insertion_point(class_scope:indoor_data_historical.Request)
  ))
_sym_db.RegisterMessage(Request)

Setpoint = _reflection.GeneratedProtocolMessageType('Setpoint', (_message.Message,), dict(
  DESCRIPTOR = _SETPOINT,
  __module__ = 'indoor_data_historical_pb2'
  # @@protoc_insertion_point(class_scope:indoor_data_historical.Setpoint)
  ))
_sym_db.RegisterMessage(Setpoint)

TemperaturePoint = _reflection.GeneratedProtocolMessageType('TemperaturePoint', (_message.Message,), dict(
  DESCRIPTOR = _TEMPERATUREPOINT,
  __module__ = 'indoor_data_historical_pb2'
  # @@protoc_insertion_point(class_scope:indoor_data_historical.TemperaturePoint)
  ))
_sym_db.RegisterMessage(TemperaturePoint)

ActionPoint = _reflection.GeneratedProtocolMessageType('ActionPoint', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONPOINT,
  __module__ = 'indoor_data_historical_pb2'
  # @@protoc_insertion_point(class_scope:indoor_data_historical.ActionPoint)
  ))
_sym_db.RegisterMessage(ActionPoint)

RawTemperatureReply = _reflection.GeneratedProtocolMessageType('RawTemperatureReply', (_message.Message,), dict(
  DESCRIPTOR = _RAWTEMPERATUREREPLY,
  __module__ = 'indoor_data_historical_pb2'
  # @@protoc_insertion_point(class_scope:indoor_data_historical.RawTemperatureReply)
  ))
_sym_db.RegisterMessage(RawTemperatureReply)

RawActionReply = _reflection.GeneratedProtocolMessageType('RawActionReply', (_message.Message,), dict(
  DESCRIPTOR = _RAWACTIONREPLY,
  __module__ = 'indoor_data_historical_pb2'
  # @@protoc_insertion_point(class_scope:indoor_data_historical.RawActionReply)
  ))
_sym_db.RegisterMessage(RawActionReply)

RawTemperatureBandsReply = _reflection.GeneratedProtocolMessageType('RawTemperatureBandsReply', (_message.Message,), dict(
  DESCRIPTOR = _RAWTEMPERATUREBANDSREPLY,
  __module__ = 'indoor_data_historical_pb2'
  # @@protoc_insertion_point(class_scope:indoor_data_historical.RawTemperatureBandsReply)
  ))
_sym_db.RegisterMessage(RawTemperatureBandsReply)


DESCRIPTOR._options = None

_INDOORDATAHISTORICAL = _descriptor.ServiceDescriptor(
  name='IndoorDataHistorical',
  full_name='indoor_data_historical.IndoorDataHistorical',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=610,
  serialized_end=937,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRawTemperatures',
    full_name='indoor_data_historical.IndoorDataHistorical.GetRawTemperatures',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RAWTEMPERATUREREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRawActions',
    full_name='indoor_data_historical.IndoorDataHistorical.GetRawActions',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RAWACTIONREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRawTemperatureBands',
    full_name='indoor_data_historical.IndoorDataHistorical.GetRawTemperatureBands',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RAWTEMPERATUREBANDSREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INDOORDATAHISTORICAL)

DESCRIPTOR.services_by_name['IndoorDataHistorical'] = _INDOORDATAHISTORICAL

# @@protoc_insertion_point(module_scope)
