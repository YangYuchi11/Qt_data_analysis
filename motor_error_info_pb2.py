# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: motor_error_info.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16motor_error_info.proto\x12\tcomm_data\"\\\n\x0eMotorErrorInfo\x12\'\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x19.comm_data.MotorErrorCode\x12\x10\n\x08\x63ode_raw\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\t*\x87\x02\n\x0eMotorErrorCode\x12\x12\n\x0eMOTOR_NO_ERROR\x10\x00\x12\x16\n\x12MOTOR_OVER_VOLTAGE\x10\x01\x12\x17\n\x13MOTOR_UNDER_VOLTAGE\x10\x02\x12\x16\n\x12MOTOR_EEPROM_ERROR\x10\x03\x12\x16\n\x12MOTOR_OVER_CURRENT\x10\x04\x12\x1a\n\x16MOTOR_OVER_TEMPERATURE\x10\x05\x12\x16\n\x12MOTOR_CAN_TIME_OUT\x10\x06\x12\x1c\n\x18MOTOR_OUTPUT_VOLTAGE_LOW\x10\x07\x12\x15\n\x11MOTOR_OTHER_ERROR\x10\x64\x12\x17\n\x12MOTOR_UNKNOW_ERROR\x10\xff\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'motor_error_info_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MOTORERRORCODE._serialized_start=132
  _MOTORERRORCODE._serialized_end=395
  _MOTORERRORINFO._serialized_start=37
  _MOTORERRORINFO._serialized_end=129
# @@protoc_insertion_point(module_scope)