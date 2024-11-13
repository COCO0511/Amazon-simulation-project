# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: amazon_ups.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='amazon_ups.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x61mazon_ups.proto\"\xab\x01\n\rrequest_truck\x12\x12\n\npackage_id\x18\x01 \x02(\x03\x12\x14\n\x0cwarehouse_id\x18\x02 \x02(\x03\x12\x10\n\x08ups_user\x18\x03 \x01(\t\x12\x13\n\x0bwarehouse_x\x18\x04 \x02(\x03\x12\x13\n\x0bwarehouse_y\x18\x05 \x02(\x03\x12\x0e\n\x06\x64\x65st_x\x18\x06 \x02(\x03\x12\x0e\n\x06\x64\x65st_y\x18\x07 \x02(\x03\x12\x14\n\x05items\x18\x08 \x03(\x0b\x32\x05.Item\"&\n\x04Item\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08quantity\x18\x02 \x02(\x03\"T\n\x0cload_package\x12\x12\n\npackage_id\x18\x01 \x02(\x03\x12\x0e\n\x06\x64\x65st_x\x18\x02 \x02(\x03\x12\x0e\n\x06\x64\x65st_y\x18\x03 \x02(\x03\x12\x10\n\x08truck_id\x18\x04 \x02(\x03\"X\n\x1arequest_destination_change\x12\x12\n\npackage_id\x18\x01 \x02(\x03\x12\x12\n\nnew_dest_x\x18\x02 \x02(\x03\x12\x12\n\nnew_dest_y\x18\x03 \x02(\x03\"\xa6\x01\n\nAUCommands\x12\x11\n\tconnected\x18\x01 \x01(\x08\x12!\n\ttruck_req\x18\x02 \x01(\x0b\x32\x0e.request_truck\x12 \n\tload_pack\x18\x03 \x01(\x0b\x32\r.load_package\x12,\n\x07\x64\x65st_ch\x18\x04 \x01(\x0b\x32\x1b.request_destination_change\x12\x12\n\ndisconnect\x18\x05 \x01(\x08\"}\n\x15response_truck_arrive\x12\x10\n\x08truck_id\x18\x01 \x02(\x03\x12\x13\n\x0bwarehouse_x\x18\x02 \x02(\x03\x12\x13\n\x0bwarehouse_y\x18\x03 \x02(\x03\x12\x14\n\x0cwarehouse_id\x18\x04 \x02(\x03\x12\x12\n\npackage_id\x18\x05 \x02(\x03\"#\n\rstart_deliver\x12\x12\n\npackage_id\x18\x01 \x03(\x03\"Y\n\x11\x64\x65livered_package\x12\x10\n\x08truck_id\x18\x01 \x02(\x03\x12\x12\n\npackage_id\x18\x02 \x02(\x03\x12\x0e\n\x06\x64\x65st_x\x18\x03 \x02(\x03\x12\x0e\n\x06\x64\x65st_y\x18\x04 \x02(\x03\"k\n\x1cresponse_destination_changed\x12\x12\n\npackage_id\x18\x01 \x02(\x03\x12\x12\n\nnew_dest_x\x18\x02 \x02(\x03\x12\x12\n\nnew_dest_y\x18\x03 \x02(\x03\x12\x0f\n\x07success\x18\x04 \x02(\x08\"g\n\x17msg_destination_changed\x12\x10\n\x08ups_user\x18\x01 \x02(\t\x12\x12\n\npackage_id\x18\x02 \x02(\x03\x12\x12\n\nnew_dest_x\x18\x03 \x02(\x03\x12\x12\n\nnew_dest_y\x18\x04 \x02(\x03\"\xa1\x02\n\nUACommands\x12\x10\n\x08world_id\x18\x01 \x01(\x03\x12,\n\x0ctruck_arrive\x18\x02 \x01(\x0b\x32\x16.response_truck_arrive\x12%\n\rstart_deliver\x18\x03 \x01(\x0b\x32\x0e.start_deliver\x12-\n\x11package_delivered\x18\x04 \x01(\x0b\x32\x12.delivered_package\x12\x34\n\rdest_response\x18\x05 \x01(\x0b\x32\x1d.response_destination_changed\x12\x33\n\x11\x64\x65st_notification\x18\x06 \x01(\x0b\x32\x18.msg_destination_changed\x12\x12\n\ndisconnect\x18\x07 \x01(\x08')
)




_REQUEST_TRUCK = _descriptor.Descriptor(
  name='request_truck',
  full_name='request_truck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_id', full_name='request_truck.package_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warehouse_id', full_name='request_truck.warehouse_id', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ups_user', full_name='request_truck.ups_user', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warehouse_x', full_name='request_truck.warehouse_x', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warehouse_y', full_name='request_truck.warehouse_y', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_x', full_name='request_truck.dest_x', index=5,
      number=6, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_y', full_name='request_truck.dest_y', index=6,
      number=7, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='items', full_name='request_truck.items', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=192,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Item.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='Item.quantity', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=232,
)


_LOAD_PACKAGE = _descriptor.Descriptor(
  name='load_package',
  full_name='load_package',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_id', full_name='load_package.package_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_x', full_name='load_package.dest_x', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_y', full_name='load_package.dest_y', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='truck_id', full_name='load_package.truck_id', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=318,
)


_REQUEST_DESTINATION_CHANGE = _descriptor.Descriptor(
  name='request_destination_change',
  full_name='request_destination_change',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_id', full_name='request_destination_change.package_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_dest_x', full_name='request_destination_change.new_dest_x', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_dest_y', full_name='request_destination_change.new_dest_y', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=408,
)


_AUCOMMANDS = _descriptor.Descriptor(
  name='AUCommands',
  full_name='AUCommands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connected', full_name='AUCommands.connected', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='truck_req', full_name='AUCommands.truck_req', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='load_pack', full_name='AUCommands.load_pack', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_ch', full_name='AUCommands.dest_ch', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disconnect', full_name='AUCommands.disconnect', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=577,
)


_RESPONSE_TRUCK_ARRIVE = _descriptor.Descriptor(
  name='response_truck_arrive',
  full_name='response_truck_arrive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truck_id', full_name='response_truck_arrive.truck_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warehouse_x', full_name='response_truck_arrive.warehouse_x', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warehouse_y', full_name='response_truck_arrive.warehouse_y', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warehouse_id', full_name='response_truck_arrive.warehouse_id', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_id', full_name='response_truck_arrive.package_id', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=579,
  serialized_end=704,
)


_START_DELIVER = _descriptor.Descriptor(
  name='start_deliver',
  full_name='start_deliver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_id', full_name='start_deliver.package_id', index=0,
      number=1, type=3, cpp_type=2, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=706,
  serialized_end=741,
)


_DELIVERED_PACKAGE = _descriptor.Descriptor(
  name='delivered_package',
  full_name='delivered_package',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='truck_id', full_name='delivered_package.truck_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_id', full_name='delivered_package.package_id', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_x', full_name='delivered_package.dest_x', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_y', full_name='delivered_package.dest_y', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=743,
  serialized_end=832,
)


_RESPONSE_DESTINATION_CHANGED = _descriptor.Descriptor(
  name='response_destination_changed',
  full_name='response_destination_changed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_id', full_name='response_destination_changed.package_id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_dest_x', full_name='response_destination_changed.new_dest_x', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_dest_y', full_name='response_destination_changed.new_dest_y', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='response_destination_changed.success', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=834,
  serialized_end=941,
)


_MSG_DESTINATION_CHANGED = _descriptor.Descriptor(
  name='msg_destination_changed',
  full_name='msg_destination_changed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ups_user', full_name='msg_destination_changed.ups_user', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_id', full_name='msg_destination_changed.package_id', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_dest_x', full_name='msg_destination_changed.new_dest_x', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_dest_y', full_name='msg_destination_changed.new_dest_y', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=943,
  serialized_end=1046,
)


_UACOMMANDS = _descriptor.Descriptor(
  name='UACommands',
  full_name='UACommands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='world_id', full_name='UACommands.world_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='truck_arrive', full_name='UACommands.truck_arrive', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_deliver', full_name='UACommands.start_deliver', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_delivered', full_name='UACommands.package_delivered', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_response', full_name='UACommands.dest_response', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_notification', full_name='UACommands.dest_notification', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disconnect', full_name='UACommands.disconnect', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1049,
  serialized_end=1338,
)

_REQUEST_TRUCK.fields_by_name['items'].message_type = _ITEM
_AUCOMMANDS.fields_by_name['truck_req'].message_type = _REQUEST_TRUCK
_AUCOMMANDS.fields_by_name['load_pack'].message_type = _LOAD_PACKAGE
_AUCOMMANDS.fields_by_name['dest_ch'].message_type = _REQUEST_DESTINATION_CHANGE
_UACOMMANDS.fields_by_name['truck_arrive'].message_type = _RESPONSE_TRUCK_ARRIVE
_UACOMMANDS.fields_by_name['start_deliver'].message_type = _START_DELIVER
_UACOMMANDS.fields_by_name['package_delivered'].message_type = _DELIVERED_PACKAGE
_UACOMMANDS.fields_by_name['dest_response'].message_type = _RESPONSE_DESTINATION_CHANGED
_UACOMMANDS.fields_by_name['dest_notification'].message_type = _MSG_DESTINATION_CHANGED
DESCRIPTOR.message_types_by_name['request_truck'] = _REQUEST_TRUCK
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['load_package'] = _LOAD_PACKAGE
DESCRIPTOR.message_types_by_name['request_destination_change'] = _REQUEST_DESTINATION_CHANGE
DESCRIPTOR.message_types_by_name['AUCommands'] = _AUCOMMANDS
DESCRIPTOR.message_types_by_name['response_truck_arrive'] = _RESPONSE_TRUCK_ARRIVE
DESCRIPTOR.message_types_by_name['start_deliver'] = _START_DELIVER
DESCRIPTOR.message_types_by_name['delivered_package'] = _DELIVERED_PACKAGE
DESCRIPTOR.message_types_by_name['response_destination_changed'] = _RESPONSE_DESTINATION_CHANGED
DESCRIPTOR.message_types_by_name['msg_destination_changed'] = _MSG_DESTINATION_CHANGED
DESCRIPTOR.message_types_by_name['UACommands'] = _UACOMMANDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

request_truck = _reflection.GeneratedProtocolMessageType('request_truck', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST_TRUCK,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:request_truck)
  ))
_sym_db.RegisterMessage(request_truck)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
  DESCRIPTOR = _ITEM,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:Item)
  ))
_sym_db.RegisterMessage(Item)

load_package = _reflection.GeneratedProtocolMessageType('load_package', (_message.Message,), dict(
  DESCRIPTOR = _LOAD_PACKAGE,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:load_package)
  ))
_sym_db.RegisterMessage(load_package)

request_destination_change = _reflection.GeneratedProtocolMessageType('request_destination_change', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST_DESTINATION_CHANGE,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:request_destination_change)
  ))
_sym_db.RegisterMessage(request_destination_change)

AUCommands = _reflection.GeneratedProtocolMessageType('AUCommands', (_message.Message,), dict(
  DESCRIPTOR = _AUCOMMANDS,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:AUCommands)
  ))
_sym_db.RegisterMessage(AUCommands)

response_truck_arrive = _reflection.GeneratedProtocolMessageType('response_truck_arrive', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE_TRUCK_ARRIVE,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:response_truck_arrive)
  ))
_sym_db.RegisterMessage(response_truck_arrive)

start_deliver = _reflection.GeneratedProtocolMessageType('start_deliver', (_message.Message,), dict(
  DESCRIPTOR = _START_DELIVER,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:start_deliver)
  ))
_sym_db.RegisterMessage(start_deliver)

delivered_package = _reflection.GeneratedProtocolMessageType('delivered_package', (_message.Message,), dict(
  DESCRIPTOR = _DELIVERED_PACKAGE,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:delivered_package)
  ))
_sym_db.RegisterMessage(delivered_package)

response_destination_changed = _reflection.GeneratedProtocolMessageType('response_destination_changed', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE_DESTINATION_CHANGED,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:response_destination_changed)
  ))
_sym_db.RegisterMessage(response_destination_changed)

msg_destination_changed = _reflection.GeneratedProtocolMessageType('msg_destination_changed', (_message.Message,), dict(
  DESCRIPTOR = _MSG_DESTINATION_CHANGED,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:msg_destination_changed)
  ))
_sym_db.RegisterMessage(msg_destination_changed)

UACommands = _reflection.GeneratedProtocolMessageType('UACommands', (_message.Message,), dict(
  DESCRIPTOR = _UACOMMANDS,
  __module__ = 'amazon_ups_pb2'
  # @@protoc_insertion_point(class_scope:UACommands)
  ))
_sym_db.RegisterMessage(UACommands)


# @@protoc_insertion_point(module_scope)