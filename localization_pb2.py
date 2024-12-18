# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: localization.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import point3d_pb2 as point3d__pb2
import header_pb2 as header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12localization.proto\x12\tcomm_data\x1a\rpoint3d.proto\x1a\x0cheader.proto\"h\n\x05WGS84\x12\x11\n\tlongitude\x18\x01 \x01(\x01\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x01\x12\x0b\n\x03yaw\x18\x04 \x01(\x01\x12\r\n\x05pitch\x18\x05 \x01(\x01\x12\x0c\n\x04roll\x18\x06 \x01(\x01\"D\n\x03\x45NU\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\r\n\x05speed\x18\x04 \x01(\x01\x12\r\n\x05theta\x18\x05 \x01(\x01\"d\n\x03IMU\x12/\n\x13linear_acceleration\x18\x01 \x01(\x0b\x32\x12.comm_data.Point3D\x12,\n\x10\x61ngular_velocity\x18\x02 \x01(\x0b\x32\x12.comm_data.Point3D\"\xbd\x01\n\x1aLocalizationSupplementInfo\x12\x15\n\rsatellite_cnt\x18\x01 \x01(\x05\x12!\n\x19\x62\x61se_station_signal_delay\x18\x02 \x01(\x01\x12\x1c\n\x14satellite_diff_state\x18\x03 \x01(\x05\x12\x17\n\x0fheading_failure\x18\x04 \x01(\x05\x12\x1c\n\x14localization_failure\x18\x05 \x01(\x05\x12\x10\n\x08utm_time\x18\x06 \x01(\x01\"\xcc\x01\n\x0cLocalization\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x11.comm_data.Header\x12\x1f\n\x05wgs84\x18\x02 \x01(\x0b\x32\x10.comm_data.WGS84\x12\x1b\n\x03\x65nu\x18\x03 \x01(\x0b\x32\x0e.comm_data.ENU\x12\x1b\n\x03imu\x18\x04 \x01(\x0b\x32\x0e.comm_data.IMU\x12>\n\x0fsupplement_info\x18\n \x01(\x0b\x32%.comm_data.LocalizationSupplementInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'localization_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WGS84._serialized_start=62
  _WGS84._serialized_end=166
  _ENU._serialized_start=168
  _ENU._serialized_end=236
  _IMU._serialized_start=238
  _IMU._serialized_end=338
  _LOCALIZATIONSUPPLEMENTINFO._serialized_start=341
  _LOCALIZATIONSUPPLEMENTINFO._serialized_end=530
  _LOCALIZATION._serialized_start=533
  _LOCALIZATION._serialized_end=737
# @@protoc_insertion_point(module_scope)
