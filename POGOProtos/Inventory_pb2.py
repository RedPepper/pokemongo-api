# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos.Inventory.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Inventory import Item_pb2 as POGOProtos_dot_Inventory_dot_Item__pb2
from POGOProtos import Enums_pb2 as POGOProtos_dot_Enums__pb2
from POGOProtos.Data import Avatar_pb2 as POGOProtos_dot_Data_dot_Avatar__pb2
from POGOProtos import Data_pb2 as POGOProtos_dot_Data__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Data_dot_Player__pb2 = POGOProtos_dot_Data__pb2.POGOProtos_dot_Data_dot_Player__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Inventory_dot_Item__pb2 = POGOProtos_dot_Data__pb2.POGOProtos_dot_Inventory_dot_Item__pb2
from POGOProtos.Data import Player_pb2 as POGOProtos_dot_Data_dot_Player__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data_dot_Player__pb2.POGOProtos_dot_Enums__pb2
from POGOProtos.Data import Quests_pb2 as POGOProtos_dot_Data_dot_Quests__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data_dot_Quests__pb2.POGOProtos_dot_Enums__pb2

from POGOProtos.Inventory.Item_pb2 import *
from POGOProtos.Enums_pb2 import *
from POGOProtos.Data.Avatar_pb2 import *
from POGOProtos.Data_pb2 import *
from POGOProtos.Data.Player_pb2 import *
from POGOProtos.Data.Quests_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos.Inventory.proto',
  package='POGOProtos.Inventory',
  syntax='proto3',
  serialized_pb=_b('\n\x1aPOGOProtos.Inventory.proto\x12\x14POGOProtos.Inventory\x1a\x1fPOGOProtos.Inventory.Item.proto\x1a\x16POGOProtos.Enums.proto\x1a\x1cPOGOProtos.Data.Avatar.proto\x1a\x15POGOProtos.Data.proto\x1a\x1cPOGOProtos.Data.Player.proto\x1a\x1cPOGOProtos.Data.Quests.proto\"\xa0\x01\n\x0b\x41ppliedItem\x12\x32\n\x07item_id\x18\x01 \x01(\x0e\x32!.POGOProtos.Inventory.Item.ItemId\x12\x36\n\titem_type\x18\x02 \x01(\x0e\x32#.POGOProtos.Inventory.Item.ItemType\x12\x11\n\texpire_ms\x18\x03 \x01(\x03\x12\x12\n\napplied_ms\x18\x04 \x01(\x03\"?\n\x0c\x41ppliedItems\x12/\n\x04item\x18\x04 \x03(\x0b\x32!.POGOProtos.Inventory.AppliedItem\"L\n\x05\x43\x61ndy\x12\x34\n\tfamily_id\x18\x01 \x01(\x0e\x32!.POGOProtos.Enums.PokemonFamilyId\x12\r\n\x05\x63\x61ndy\x18\x02 \x01(\x05\"\xed\x01\n\x0c\x45ggIncubator\x12\n\n\x02id\x18\x01 \x01(\t\x12\x32\n\x07item_id\x18\x02 \x01(\x0e\x32!.POGOProtos.Inventory.Item.ItemId\x12>\n\x0eincubator_type\x18\x03 \x01(\x0e\x32&.POGOProtos.Inventory.EggIncubatorType\x12\x16\n\x0euses_remaining\x18\x04 \x01(\x05\x12\x12\n\npokemon_id\x18\x05 \x01(\x04\x12\x17\n\x0fstart_km_walked\x18\x06 \x01(\x01\x12\x18\n\x10target_km_walked\x18\x07 \x01(\x01\"J\n\rEggIncubators\x12\x39\n\regg_incubator\x18\x01 \x03(\x0b\x32\".POGOProtos.Inventory.EggIncubator\"\x87\x01\n\x0eInventoryDelta\x12\x1d\n\x15original_timestamp_ms\x18\x01 \x01(\x03\x12\x18\n\x10new_timestamp_ms\x18\x02 \x01(\x03\x12<\n\x0finventory_items\x18\x03 \x03(\x0b\x32#.POGOProtos.Inventory.InventoryItem\"\xde\x01\n\rInventoryItem\x12\x1d\n\x15modified_timestamp_ms\x18\x01 \x01(\x03\x12\x45\n\x0c\x64\x65leted_item\x18\x02 \x01(\x0b\x32/.POGOProtos.Inventory.InventoryItem.DeletedItem\x12\x44\n\x13inventory_item_data\x18\x03 \x01(\x0b\x32\'.POGOProtos.Inventory.InventoryItemData\x1a!\n\x0b\x44\x65letedItem\x12\x12\n\npokemon_id\x18\x01 \x01(\x06\"\xb9\x05\n\x11InventoryItemData\x12\x32\n\x0cpokemon_data\x18\x01 \x01(\x0b\x32\x1c.POGOProtos.Data.PokemonData\x12\x31\n\x04item\x18\x02 \x01(\x0b\x32#.POGOProtos.Inventory.Item.ItemData\x12\x34\n\rpokedex_entry\x18\x03 \x01(\x0b\x32\x1d.POGOProtos.Data.PokedexEntry\x12\x39\n\x0cplayer_stats\x18\x04 \x01(\x0b\x32#.POGOProtos.Data.Player.PlayerStats\x12?\n\x0fplayer_currency\x18\x05 \x01(\x0b\x32&.POGOProtos.Data.Player.PlayerCurrency\x12;\n\rplayer_camera\x18\x06 \x01(\x0b\x32$.POGOProtos.Data.Player.PlayerCamera\x12\x43\n\x12inventory_upgrades\x18\x07 \x01(\x0b\x32\'.POGOProtos.Inventory.InventoryUpgrades\x12\x39\n\rapplied_items\x18\x08 \x01(\x0b\x32\".POGOProtos.Inventory.AppliedItems\x12;\n\x0e\x65gg_incubators\x18\t \x01(\x0b\x32#.POGOProtos.Inventory.EggIncubators\x12*\n\x05\x63\x61ndy\x18\n \x01(\x0b\x32\x1b.POGOProtos.Inventory.Candy\x12,\n\x05quest\x18\x0b \x01(\x0b\x32\x1d.POGOProtos.Data.Quests.Quest\x12\x37\n\x0b\x61vatar_item\x18\x0c \x01(\x0b\x32\".POGOProtos.Data.Avatar.AvatarItem\"\x89\x03\n\x0cInventoryKey\x12\x12\n\npokemon_id\x18\x01 \x01(\x06\x12/\n\x04item\x18\x02 \x01(\x0e\x32!.POGOProtos.Inventory.Item.ItemId\x12\x18\n\x10pokedex_entry_id\x18\x03 \x01(\x05\x12\x14\n\x0cplayer_stats\x18\x04 \x01(\x08\x12\x17\n\x0fplayer_currency\x18\x05 \x01(\x08\x12\x15\n\rplayer_camera\x18\x06 \x01(\x08\x12\x1a\n\x12inventory_upgrades\x18\x07 \x01(\x08\x12\x15\n\rapplied_items\x18\x08 \x01(\x08\x12\x16\n\x0e\x65gg_incubators\x18\t \x01(\x08\x12<\n\x11pokemon_family_id\x18\n \x01(\x0e\x32!.POGOProtos.Enums.PokemonFamilyId\x12/\n\nquest_type\x18\x0b \x01(\x0e\x32\x1b.POGOProtos.Enums.QuestType\x12\x1a\n\x12\x61vatar_template_id\x18\x0c \x01(\t\"\xa4\x01\n\x10InventoryUpgrade\x12\x32\n\x07item_id\x18\x01 \x01(\x0e\x32!.POGOProtos.Inventory.Item.ItemId\x12@\n\x0cupgrade_type\x18\x02 \x01(\x0e\x32*.POGOProtos.Inventory.InventoryUpgradeType\x12\x1a\n\x12\x61\x64\x64itional_storage\x18\x03 \x01(\x05\"W\n\x11InventoryUpgrades\x12\x42\n\x12inventory_upgrades\x18\x01 \x03(\x0b\x32&.POGOProtos.Inventory.InventoryUpgrade*?\n\x10\x45ggIncubatorType\x12\x13\n\x0fINCUBATOR_UNSET\x10\x00\x12\x16\n\x12INCUBATOR_DISTANCE\x10\x01*b\n\x14InventoryUpgradeType\x12\x11\n\rUPGRADE_UNSET\x10\x00\x12\x19\n\x15INCREASE_ITEM_STORAGE\x10\x01\x12\x1c\n\x18INCREASE_POKEMON_STORAGE\x10\x02P\x00P\x01P\x02P\x03P\x04P\x05\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Inventory_dot_Item__pb2.DESCRIPTOR,POGOProtos_dot_Enums__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Avatar__pb2.DESCRIPTOR,POGOProtos_dot_Data__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Player__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Quests__pb2.DESCRIPTOR,],
  public_dependencies=[POGOProtos_dot_Inventory_dot_Item__pb2.DESCRIPTOR,POGOProtos_dot_Enums__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Avatar__pb2.DESCRIPTOR,POGOProtos_dot_Data__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Player__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Quests__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_EGGINCUBATORTYPE = _descriptor.EnumDescriptor(
  name='EggIncubatorType',
  full_name='POGOProtos.Inventory.EggIncubatorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INCUBATOR_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCUBATOR_DISTANCE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2559,
  serialized_end=2622,
)
_sym_db.RegisterEnumDescriptor(_EGGINCUBATORTYPE)

EggIncubatorType = enum_type_wrapper.EnumTypeWrapper(_EGGINCUBATORTYPE)
_INVENTORYUPGRADETYPE = _descriptor.EnumDescriptor(
  name='InventoryUpgradeType',
  full_name='POGOProtos.Inventory.InventoryUpgradeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UPGRADE_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCREASE_ITEM_STORAGE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCREASE_POKEMON_STORAGE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2624,
  serialized_end=2722,
)
_sym_db.RegisterEnumDescriptor(_INVENTORYUPGRADETYPE)

InventoryUpgradeType = enum_type_wrapper.EnumTypeWrapper(_INVENTORYUPGRADETYPE)
INCUBATOR_UNSET = 0
INCUBATOR_DISTANCE = 1
UPGRADE_UNSET = 0
INCREASE_ITEM_STORAGE = 1
INCREASE_POKEMON_STORAGE = 2



_APPLIEDITEM = _descriptor.Descriptor(
  name='AppliedItem',
  full_name='POGOProtos.Inventory.AppliedItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='POGOProtos.Inventory.AppliedItem.item_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_type', full_name='POGOProtos.Inventory.AppliedItem.item_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expire_ms', full_name='POGOProtos.Inventory.AppliedItem.expire_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applied_ms', full_name='POGOProtos.Inventory.AppliedItem.applied_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=383,
)


_APPLIEDITEMS = _descriptor.Descriptor(
  name='AppliedItems',
  full_name='POGOProtos.Inventory.AppliedItems',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='POGOProtos.Inventory.AppliedItems.item', index=0,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=385,
  serialized_end=448,
)


_CANDY = _descriptor.Descriptor(
  name='Candy',
  full_name='POGOProtos.Inventory.Candy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='family_id', full_name='POGOProtos.Inventory.Candy.family_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candy', full_name='POGOProtos.Inventory.Candy.candy', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=450,
  serialized_end=526,
)


_EGGINCUBATOR = _descriptor.Descriptor(
  name='EggIncubator',
  full_name='POGOProtos.Inventory.EggIncubator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='POGOProtos.Inventory.EggIncubator.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='POGOProtos.Inventory.EggIncubator.item_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='incubator_type', full_name='POGOProtos.Inventory.EggIncubator.incubator_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uses_remaining', full_name='POGOProtos.Inventory.EggIncubator.uses_remaining', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='POGOProtos.Inventory.EggIncubator.pokemon_id', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_km_walked', full_name='POGOProtos.Inventory.EggIncubator.start_km_walked', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_km_walked', full_name='POGOProtos.Inventory.EggIncubator.target_km_walked', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=766,
)


_EGGINCUBATORS = _descriptor.Descriptor(
  name='EggIncubators',
  full_name='POGOProtos.Inventory.EggIncubators',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='egg_incubator', full_name='POGOProtos.Inventory.EggIncubators.egg_incubator', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=768,
  serialized_end=842,
)


_INVENTORYDELTA = _descriptor.Descriptor(
  name='InventoryDelta',
  full_name='POGOProtos.Inventory.InventoryDelta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='original_timestamp_ms', full_name='POGOProtos.Inventory.InventoryDelta.original_timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_timestamp_ms', full_name='POGOProtos.Inventory.InventoryDelta.new_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_items', full_name='POGOProtos.Inventory.InventoryDelta.inventory_items', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=845,
  serialized_end=980,
)


_INVENTORYITEM_DELETEDITEM = _descriptor.Descriptor(
  name='DeletedItem',
  full_name='POGOProtos.Inventory.InventoryItem.DeletedItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='POGOProtos.Inventory.InventoryItem.DeletedItem.pokemon_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1172,
  serialized_end=1205,
)

_INVENTORYITEM = _descriptor.Descriptor(
  name='InventoryItem',
  full_name='POGOProtos.Inventory.InventoryItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='modified_timestamp_ms', full_name='POGOProtos.Inventory.InventoryItem.modified_timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deleted_item', full_name='POGOProtos.Inventory.InventoryItem.deleted_item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_item_data', full_name='POGOProtos.Inventory.InventoryItem.inventory_item_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_INVENTORYITEM_DELETEDITEM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=983,
  serialized_end=1205,
)


_INVENTORYITEMDATA = _descriptor.Descriptor(
  name='InventoryItemData',
  full_name='POGOProtos.Inventory.InventoryItemData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_data', full_name='POGOProtos.Inventory.InventoryItemData.pokemon_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='POGOProtos.Inventory.InventoryItemData.item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokedex_entry', full_name='POGOProtos.Inventory.InventoryItemData.pokedex_entry', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_stats', full_name='POGOProtos.Inventory.InventoryItemData.player_stats', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_currency', full_name='POGOProtos.Inventory.InventoryItemData.player_currency', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_camera', full_name='POGOProtos.Inventory.InventoryItemData.player_camera', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_upgrades', full_name='POGOProtos.Inventory.InventoryItemData.inventory_upgrades', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applied_items', full_name='POGOProtos.Inventory.InventoryItemData.applied_items', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_incubators', full_name='POGOProtos.Inventory.InventoryItemData.egg_incubators', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candy', full_name='POGOProtos.Inventory.InventoryItemData.candy', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest', full_name='POGOProtos.Inventory.InventoryItemData.quest', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_item', full_name='POGOProtos.Inventory.InventoryItemData.avatar_item', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1208,
  serialized_end=1905,
)


_INVENTORYKEY = _descriptor.Descriptor(
  name='InventoryKey',
  full_name='POGOProtos.Inventory.InventoryKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='POGOProtos.Inventory.InventoryKey.pokemon_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='POGOProtos.Inventory.InventoryKey.item', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokedex_entry_id', full_name='POGOProtos.Inventory.InventoryKey.pokedex_entry_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_stats', full_name='POGOProtos.Inventory.InventoryKey.player_stats', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_currency', full_name='POGOProtos.Inventory.InventoryKey.player_currency', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_camera', full_name='POGOProtos.Inventory.InventoryKey.player_camera', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_upgrades', full_name='POGOProtos.Inventory.InventoryKey.inventory_upgrades', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applied_items', full_name='POGOProtos.Inventory.InventoryKey.applied_items', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_incubators', full_name='POGOProtos.Inventory.InventoryKey.egg_incubators', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_family_id', full_name='POGOProtos.Inventory.InventoryKey.pokemon_family_id', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest_type', full_name='POGOProtos.Inventory.InventoryKey.quest_type', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_template_id', full_name='POGOProtos.Inventory.InventoryKey.avatar_template_id', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1908,
  serialized_end=2301,
)


_INVENTORYUPGRADE = _descriptor.Descriptor(
  name='InventoryUpgrade',
  full_name='POGOProtos.Inventory.InventoryUpgrade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='POGOProtos.Inventory.InventoryUpgrade.item_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upgrade_type', full_name='POGOProtos.Inventory.InventoryUpgrade.upgrade_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additional_storage', full_name='POGOProtos.Inventory.InventoryUpgrade.additional_storage', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2304,
  serialized_end=2468,
)


_INVENTORYUPGRADES = _descriptor.Descriptor(
  name='InventoryUpgrades',
  full_name='POGOProtos.Inventory.InventoryUpgrades',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inventory_upgrades', full_name='POGOProtos.Inventory.InventoryUpgrades.inventory_upgrades', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2470,
  serialized_end=2557,
)

_APPLIEDITEM.fields_by_name['item_id'].enum_type = POGOProtos_dot_Inventory_dot_Item__pb2._ITEMID
_APPLIEDITEM.fields_by_name['item_type'].enum_type = POGOProtos_dot_Inventory_dot_Item__pb2._ITEMTYPE
_APPLIEDITEMS.fields_by_name['item'].message_type = _APPLIEDITEM
_CANDY.fields_by_name['family_id'].enum_type = POGOProtos_dot_Enums__pb2._POKEMONFAMILYID
_EGGINCUBATOR.fields_by_name['item_id'].enum_type = POGOProtos_dot_Inventory_dot_Item__pb2._ITEMID
_EGGINCUBATOR.fields_by_name['incubator_type'].enum_type = _EGGINCUBATORTYPE
_EGGINCUBATORS.fields_by_name['egg_incubator'].message_type = _EGGINCUBATOR
_INVENTORYDELTA.fields_by_name['inventory_items'].message_type = _INVENTORYITEM
_INVENTORYITEM_DELETEDITEM.containing_type = _INVENTORYITEM
_INVENTORYITEM.fields_by_name['deleted_item'].message_type = _INVENTORYITEM_DELETEDITEM
_INVENTORYITEM.fields_by_name['inventory_item_data'].message_type = _INVENTORYITEMDATA
_INVENTORYITEMDATA.fields_by_name['pokemon_data'].message_type = POGOProtos_dot_Data__pb2._POKEMONDATA
_INVENTORYITEMDATA.fields_by_name['item'].message_type = POGOProtos_dot_Inventory_dot_Item__pb2._ITEMDATA
_INVENTORYITEMDATA.fields_by_name['pokedex_entry'].message_type = POGOProtos_dot_Data__pb2._POKEDEXENTRY
_INVENTORYITEMDATA.fields_by_name['player_stats'].message_type = POGOProtos_dot_Data_dot_Player__pb2._PLAYERSTATS
_INVENTORYITEMDATA.fields_by_name['player_currency'].message_type = POGOProtos_dot_Data_dot_Player__pb2._PLAYERCURRENCY
_INVENTORYITEMDATA.fields_by_name['player_camera'].message_type = POGOProtos_dot_Data_dot_Player__pb2._PLAYERCAMERA
_INVENTORYITEMDATA.fields_by_name['inventory_upgrades'].message_type = _INVENTORYUPGRADES
_INVENTORYITEMDATA.fields_by_name['applied_items'].message_type = _APPLIEDITEMS
_INVENTORYITEMDATA.fields_by_name['egg_incubators'].message_type = _EGGINCUBATORS
_INVENTORYITEMDATA.fields_by_name['candy'].message_type = _CANDY
_INVENTORYITEMDATA.fields_by_name['quest'].message_type = POGOProtos_dot_Data_dot_Quests__pb2._QUEST
_INVENTORYITEMDATA.fields_by_name['avatar_item'].message_type = POGOProtos_dot_Data_dot_Avatar__pb2._AVATARITEM
_INVENTORYKEY.fields_by_name['item'].enum_type = POGOProtos_dot_Inventory_dot_Item__pb2._ITEMID
_INVENTORYKEY.fields_by_name['pokemon_family_id'].enum_type = POGOProtos_dot_Enums__pb2._POKEMONFAMILYID
_INVENTORYKEY.fields_by_name['quest_type'].enum_type = POGOProtos_dot_Enums__pb2._QUESTTYPE
_INVENTORYUPGRADE.fields_by_name['item_id'].enum_type = POGOProtos_dot_Inventory_dot_Item__pb2._ITEMID
_INVENTORYUPGRADE.fields_by_name['upgrade_type'].enum_type = _INVENTORYUPGRADETYPE
_INVENTORYUPGRADES.fields_by_name['inventory_upgrades'].message_type = _INVENTORYUPGRADE
DESCRIPTOR.message_types_by_name['AppliedItem'] = _APPLIEDITEM
DESCRIPTOR.message_types_by_name['AppliedItems'] = _APPLIEDITEMS
DESCRIPTOR.message_types_by_name['Candy'] = _CANDY
DESCRIPTOR.message_types_by_name['EggIncubator'] = _EGGINCUBATOR
DESCRIPTOR.message_types_by_name['EggIncubators'] = _EGGINCUBATORS
DESCRIPTOR.message_types_by_name['InventoryDelta'] = _INVENTORYDELTA
DESCRIPTOR.message_types_by_name['InventoryItem'] = _INVENTORYITEM
DESCRIPTOR.message_types_by_name['InventoryItemData'] = _INVENTORYITEMDATA
DESCRIPTOR.message_types_by_name['InventoryKey'] = _INVENTORYKEY
DESCRIPTOR.message_types_by_name['InventoryUpgrade'] = _INVENTORYUPGRADE
DESCRIPTOR.message_types_by_name['InventoryUpgrades'] = _INVENTORYUPGRADES
DESCRIPTOR.enum_types_by_name['EggIncubatorType'] = _EGGINCUBATORTYPE
DESCRIPTOR.enum_types_by_name['InventoryUpgradeType'] = _INVENTORYUPGRADETYPE

AppliedItem = _reflection.GeneratedProtocolMessageType('AppliedItem', (_message.Message,), dict(
  DESCRIPTOR = _APPLIEDITEM,
  __module__ = 'POGOProtos.Inventory_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.AppliedItem)
  ))
_sym_db.RegisterMessage(AppliedItem)

AppliedItems = _reflection.GeneratedProtocolMessageType('AppliedItems', (_message.Message,), dict(
  DESCRIPTOR = _APPLIEDITEMS,
  __module__ = 'POGOProtos.Inventory_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.AppliedItems)
  ))
_sym_db.RegisterMessage(AppliedItems)

Candy = _reflection.GeneratedProtocolMessageType('Candy', (_message.Message,), dict(
  DESCRIPTOR = _CANDY,
  __module__ = 'POGOProtos.Inventory_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.Candy)
  ))
_sym_db.RegisterMessage(Candy)

EggIncubator = _reflection.GeneratedProtocolMessageType('EggIncubator', (_message.Message,), dict(
  DESCRIPTOR = _EGGINCUBATOR,
  __module__ = 'POGOProtos.Inventory_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.EggIncubator)
  ))
_sym_db.RegisterMessage(EggIncubator)

EggIncubators = _reflection.GeneratedProtocolMessageType('EggIncubators', (_message.Message,), dict(
  DESCRIPTOR = _EGGINCUBATORS,
  __module__ = 'POGOProtos.Inventory_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.EggIncubators)
  ))
_sym_db.RegisterMessage(EggIncubators)

InventoryDelta = _reflection.GeneratedProtocolMessageType('InventoryDelta', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYDELTA,
  __module__ = 'POGOProtos.Inventory_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.InventoryDelta)
  ))
_sym_db.RegisterMessage(InventoryDelta)

InventoryItem = _reflection.GeneratedProtocolMessageType('InventoryItem', (_message.Message,), dict(

  DeletedItem = _reflection.GeneratedProtocolMessageType('DeletedItem', (_message.Message,), dict(
    DESCRIPTOR = _INVENTORYITEM_DELETEDITEM,
    __module__ = 'POGOProtos.Inventory_pb2'
    # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.InventoryItem.DeletedItem)
    ))
  ,
  DESCRIPTOR = _INVENTORYITEM,
  __module__ = 'POGOProtos.Inventory_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.InventoryItem)
  ))
_sym_db.RegisterMessage(InventoryItem)
_sym_db.RegisterMessage(InventoryItem.DeletedItem)

InventoryItemData = _reflection.GeneratedProtocolMessageType('InventoryItemData', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYITEMDATA,
  __module__ = 'POGOProtos.Inventory_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.InventoryItemData)
  ))
_sym_db.RegisterMessage(InventoryItemData)

InventoryKey = _reflection.GeneratedProtocolMessageType('InventoryKey', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYKEY,
  __module__ = 'POGOProtos.Inventory_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.InventoryKey)
  ))
_sym_db.RegisterMessage(InventoryKey)

InventoryUpgrade = _reflection.GeneratedProtocolMessageType('InventoryUpgrade', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYUPGRADE,
  __module__ = 'POGOProtos.Inventory_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.InventoryUpgrade)
  ))
_sym_db.RegisterMessage(InventoryUpgrade)

InventoryUpgrades = _reflection.GeneratedProtocolMessageType('InventoryUpgrades', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYUPGRADES,
  __module__ = 'POGOProtos.Inventory_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.InventoryUpgrades)
  ))
_sym_db.RegisterMessage(InventoryUpgrades)


# @@protoc_insertion_point(module_scope)
