# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos.Settings.proto

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
  name='POGOProtos.Settings.proto',
  package='POGOProtos.Settings',
  syntax='proto3',
  serialized_pb=_b('\n\x19POGOProtos.Settings.proto\x12\x13POGOProtos.Settings\"&\n\x16\x44ownloadSettingsAction\x12\x0c\n\x04hash\x18\x01 \x01(\t\"2\n\rEventSettings\x12!\n\x19\x63ondolence_ribbon_country\x18\x01 \x03(\t\"\xb0\x01\n\x10\x46\x65stivalSettings\x12I\n\rfestival_type\x18\x01 \x01(\x0e\x32\x32.POGOProtos.Settings.FestivalSettings.FestivalType\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0e\n\x06vector\x18\x03 \x01(\t\"4\n\x0c\x46\x65stivalType\x12\x08\n\x04NONE\x10\x00\x12\r\n\tHALLOWEEN\x10\x01\x12\x0b\n\x07HOLIDAY\x10\x02\"\xe4\x01\n\x0c\x46ortSettings\x12 \n\x18interaction_range_meters\x18\x01 \x01(\x01\x12\"\n\x1amax_total_deployed_pokemon\x18\x02 \x01(\x05\x12#\n\x1bmax_player_deployed_pokemon\x18\x03 \x01(\x05\x12!\n\x19\x64\x65ploy_stamina_multiplier\x18\x04 \x01(\x01\x12 \n\x18\x64\x65ploy_attack_multiplier\x18\x05 \x01(\x01\x12$\n\x1c\x66\x61r_interaction_range_meters\x18\x06 \x01(\x01\"\xaf\x04\n\x0eGlobalSettings\x12\x38\n\rfort_settings\x18\x02 \x01(\x0b\x32!.POGOProtos.Settings.FortSettings\x12\x36\n\x0cmap_settings\x18\x03 \x01(\x0b\x32 .POGOProtos.Settings.MapSettings\x12:\n\x0elevel_settings\x18\x04 \x01(\x0b\x32\".POGOProtos.Settings.LevelSettings\x12\x42\n\x12inventory_settings\x18\x05 \x01(\x0b\x32&.POGOProtos.Settings.InventorySettings\x12\x1e\n\x16minimum_client_version\x18\x06 \x01(\t\x12\x36\n\x0cgps_settings\x18\x07 \x01(\x0b\x32 .POGOProtos.Settings.GpsSettings\x12@\n\x11\x66\x65stival_settings\x18\x08 \x01(\x0b\x32%.POGOProtos.Settings.FestivalSettings\x12:\n\x0e\x65vent_settings\x18\t \x01(\x0b\x32\".POGOProtos.Settings.EventSettings\x12\x19\n\x11max_pokemon_types\x18\n \x01(\x05\x12:\n\x0esfida_settings\x18\x0b \x01(\x0b\x32\".POGOProtos.Settings.SfidaSettings\"\xbb\x01\n\x0bGpsSettings\x12/\n\'driving_warning_speed_meters_per_second\x18\x01 \x01(\x02\x12(\n driving_warning_cooldown_minutes\x18\x02 \x01(\x02\x12-\n%driving_speed_sample_interval_seconds\x18\x03 \x01(\x02\x12\"\n\x1a\x64riving_speed_sample_count\x18\x04 \x01(\x05\"\x80\x01\n\x11InventorySettings\x12\x13\n\x0bmax_pokemon\x18\x01 \x01(\x05\x12\x15\n\rmax_bag_items\x18\x02 \x01(\x05\x12\x14\n\x0c\x62\x61se_pokemon\x18\x03 \x01(\x05\x12\x16\n\x0e\x62\x61se_bag_items\x18\x04 \x01(\x05\x12\x11\n\tbase_eggs\x18\x05 \x01(\x05\"Q\n\rLevelSettings\x12\x1b\n\x13trainer_cp_modifier\x18\x02 \x01(\x01\x12#\n\x1btrainer_difficulty_modifier\x18\x03 \x01(\x01\"\xb2\x02\n\x0bMapSettings\x12\x1d\n\x15pokemon_visible_range\x18\x01 \x01(\x01\x12\x1d\n\x15poke_nav_range_meters\x18\x02 \x01(\x01\x12\x1e\n\x16\x65ncounter_range_meters\x18\x03 \x01(\x01\x12+\n#get_map_objects_min_refresh_seconds\x18\x04 \x01(\x02\x12+\n#get_map_objects_max_refresh_seconds\x18\x05 \x01(\x02\x12+\n#get_map_objects_min_distance_meters\x18\x06 \x01(\x02\x12\x1b\n\x13google_maps_api_key\x18\x07 \x01(\t\x12!\n\x19min_nearby_hide_sightings\x18\x08 \x01(\x05\".\n\rSfidaSettings\x12\x1d\n\x15low_battery_threshold\x18\x01 \x01(\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_FESTIVALSETTINGS_FESTIVALTYPE = _descriptor.EnumDescriptor(
  name='FestivalType',
  full_name='POGOProtos.Settings.FestivalSettings.FestivalType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HALLOWEEN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOLIDAY', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=267,
  serialized_end=319,
)
_sym_db.RegisterEnumDescriptor(_FESTIVALSETTINGS_FESTIVALTYPE)


_DOWNLOADSETTINGSACTION = _descriptor.Descriptor(
  name='DownloadSettingsAction',
  full_name='POGOProtos.Settings.DownloadSettingsAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='POGOProtos.Settings.DownloadSettingsAction.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=50,
  serialized_end=88,
)


_EVENTSETTINGS = _descriptor.Descriptor(
  name='EventSettings',
  full_name='POGOProtos.Settings.EventSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condolence_ribbon_country', full_name='POGOProtos.Settings.EventSettings.condolence_ribbon_country', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=90,
  serialized_end=140,
)


_FESTIVALSETTINGS = _descriptor.Descriptor(
  name='FestivalSettings',
  full_name='POGOProtos.Settings.FestivalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='festival_type', full_name='POGOProtos.Settings.FestivalSettings.festival_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='POGOProtos.Settings.FestivalSettings.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vector', full_name='POGOProtos.Settings.FestivalSettings.vector', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FESTIVALSETTINGS_FESTIVALTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=319,
)


_FORTSETTINGS = _descriptor.Descriptor(
  name='FortSettings',
  full_name='POGOProtos.Settings.FortSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='interaction_range_meters', full_name='POGOProtos.Settings.FortSettings.interaction_range_meters', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_total_deployed_pokemon', full_name='POGOProtos.Settings.FortSettings.max_total_deployed_pokemon', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_player_deployed_pokemon', full_name='POGOProtos.Settings.FortSettings.max_player_deployed_pokemon', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deploy_stamina_multiplier', full_name='POGOProtos.Settings.FortSettings.deploy_stamina_multiplier', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deploy_attack_multiplier', full_name='POGOProtos.Settings.FortSettings.deploy_attack_multiplier', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='far_interaction_range_meters', full_name='POGOProtos.Settings.FortSettings.far_interaction_range_meters', index=5,
      number=6, type=1, cpp_type=5, label=1,
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
  serialized_start=322,
  serialized_end=550,
)


_GLOBALSETTINGS = _descriptor.Descriptor(
  name='GlobalSettings',
  full_name='POGOProtos.Settings.GlobalSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_settings', full_name='POGOProtos.Settings.GlobalSettings.fort_settings', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_settings', full_name='POGOProtos.Settings.GlobalSettings.map_settings', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_settings', full_name='POGOProtos.Settings.GlobalSettings.level_settings', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_settings', full_name='POGOProtos.Settings.GlobalSettings.inventory_settings', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minimum_client_version', full_name='POGOProtos.Settings.GlobalSettings.minimum_client_version', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gps_settings', full_name='POGOProtos.Settings.GlobalSettings.gps_settings', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='festival_settings', full_name='POGOProtos.Settings.GlobalSettings.festival_settings', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_settings', full_name='POGOProtos.Settings.GlobalSettings.event_settings', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_pokemon_types', full_name='POGOProtos.Settings.GlobalSettings.max_pokemon_types', index=8,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sfida_settings', full_name='POGOProtos.Settings.GlobalSettings.sfida_settings', index=9,
      number=11, type=11, cpp_type=10, label=1,
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
  serialized_start=553,
  serialized_end=1112,
)


_GPSSETTINGS = _descriptor.Descriptor(
  name='GpsSettings',
  full_name='POGOProtos.Settings.GpsSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='driving_warning_speed_meters_per_second', full_name='POGOProtos.Settings.GpsSettings.driving_warning_speed_meters_per_second', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='driving_warning_cooldown_minutes', full_name='POGOProtos.Settings.GpsSettings.driving_warning_cooldown_minutes', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='driving_speed_sample_interval_seconds', full_name='POGOProtos.Settings.GpsSettings.driving_speed_sample_interval_seconds', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='driving_speed_sample_count', full_name='POGOProtos.Settings.GpsSettings.driving_speed_sample_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=1115,
  serialized_end=1302,
)


_INVENTORYSETTINGS = _descriptor.Descriptor(
  name='InventorySettings',
  full_name='POGOProtos.Settings.InventorySettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_pokemon', full_name='POGOProtos.Settings.InventorySettings.max_pokemon', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_bag_items', full_name='POGOProtos.Settings.InventorySettings.max_bag_items', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_pokemon', full_name='POGOProtos.Settings.InventorySettings.base_pokemon', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_bag_items', full_name='POGOProtos.Settings.InventorySettings.base_bag_items', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_eggs', full_name='POGOProtos.Settings.InventorySettings.base_eggs', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=1305,
  serialized_end=1433,
)


_LEVELSETTINGS = _descriptor.Descriptor(
  name='LevelSettings',
  full_name='POGOProtos.Settings.LevelSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trainer_cp_modifier', full_name='POGOProtos.Settings.LevelSettings.trainer_cp_modifier', index=0,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainer_difficulty_modifier', full_name='POGOProtos.Settings.LevelSettings.trainer_difficulty_modifier', index=1,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=1435,
  serialized_end=1516,
)


_MAPSETTINGS = _descriptor.Descriptor(
  name='MapSettings',
  full_name='POGOProtos.Settings.MapSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_visible_range', full_name='POGOProtos.Settings.MapSettings.pokemon_visible_range', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='poke_nav_range_meters', full_name='POGOProtos.Settings.MapSettings.poke_nav_range_meters', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encounter_range_meters', full_name='POGOProtos.Settings.MapSettings.encounter_range_meters', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_map_objects_min_refresh_seconds', full_name='POGOProtos.Settings.MapSettings.get_map_objects_min_refresh_seconds', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_map_objects_max_refresh_seconds', full_name='POGOProtos.Settings.MapSettings.get_map_objects_max_refresh_seconds', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_map_objects_min_distance_meters', full_name='POGOProtos.Settings.MapSettings.get_map_objects_min_distance_meters', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='google_maps_api_key', full_name='POGOProtos.Settings.MapSettings.google_maps_api_key', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_nearby_hide_sightings', full_name='POGOProtos.Settings.MapSettings.min_nearby_hide_sightings', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=1519,
  serialized_end=1825,
)


_SFIDASETTINGS = _descriptor.Descriptor(
  name='SfidaSettings',
  full_name='POGOProtos.Settings.SfidaSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='low_battery_threshold', full_name='POGOProtos.Settings.SfidaSettings.low_battery_threshold', index=0,
      number=1, type=2, cpp_type=6, label=1,
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
  serialized_start=1827,
  serialized_end=1873,
)

_FESTIVALSETTINGS.fields_by_name['festival_type'].enum_type = _FESTIVALSETTINGS_FESTIVALTYPE
_FESTIVALSETTINGS_FESTIVALTYPE.containing_type = _FESTIVALSETTINGS
_GLOBALSETTINGS.fields_by_name['fort_settings'].message_type = _FORTSETTINGS
_GLOBALSETTINGS.fields_by_name['map_settings'].message_type = _MAPSETTINGS
_GLOBALSETTINGS.fields_by_name['level_settings'].message_type = _LEVELSETTINGS
_GLOBALSETTINGS.fields_by_name['inventory_settings'].message_type = _INVENTORYSETTINGS
_GLOBALSETTINGS.fields_by_name['gps_settings'].message_type = _GPSSETTINGS
_GLOBALSETTINGS.fields_by_name['festival_settings'].message_type = _FESTIVALSETTINGS
_GLOBALSETTINGS.fields_by_name['event_settings'].message_type = _EVENTSETTINGS
_GLOBALSETTINGS.fields_by_name['sfida_settings'].message_type = _SFIDASETTINGS
DESCRIPTOR.message_types_by_name['DownloadSettingsAction'] = _DOWNLOADSETTINGSACTION
DESCRIPTOR.message_types_by_name['EventSettings'] = _EVENTSETTINGS
DESCRIPTOR.message_types_by_name['FestivalSettings'] = _FESTIVALSETTINGS
DESCRIPTOR.message_types_by_name['FortSettings'] = _FORTSETTINGS
DESCRIPTOR.message_types_by_name['GlobalSettings'] = _GLOBALSETTINGS
DESCRIPTOR.message_types_by_name['GpsSettings'] = _GPSSETTINGS
DESCRIPTOR.message_types_by_name['InventorySettings'] = _INVENTORYSETTINGS
DESCRIPTOR.message_types_by_name['LevelSettings'] = _LEVELSETTINGS
DESCRIPTOR.message_types_by_name['MapSettings'] = _MAPSETTINGS
DESCRIPTOR.message_types_by_name['SfidaSettings'] = _SFIDASETTINGS

DownloadSettingsAction = _reflection.GeneratedProtocolMessageType('DownloadSettingsAction', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADSETTINGSACTION,
  __module__ = 'POGOProtos.Settings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.DownloadSettingsAction)
  ))
_sym_db.RegisterMessage(DownloadSettingsAction)

EventSettings = _reflection.GeneratedProtocolMessageType('EventSettings', (_message.Message,), dict(
  DESCRIPTOR = _EVENTSETTINGS,
  __module__ = 'POGOProtos.Settings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.EventSettings)
  ))
_sym_db.RegisterMessage(EventSettings)

FestivalSettings = _reflection.GeneratedProtocolMessageType('FestivalSettings', (_message.Message,), dict(
  DESCRIPTOR = _FESTIVALSETTINGS,
  __module__ = 'POGOProtos.Settings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.FestivalSettings)
  ))
_sym_db.RegisterMessage(FestivalSettings)

FortSettings = _reflection.GeneratedProtocolMessageType('FortSettings', (_message.Message,), dict(
  DESCRIPTOR = _FORTSETTINGS,
  __module__ = 'POGOProtos.Settings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.FortSettings)
  ))
_sym_db.RegisterMessage(FortSettings)

GlobalSettings = _reflection.GeneratedProtocolMessageType('GlobalSettings', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALSETTINGS,
  __module__ = 'POGOProtos.Settings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.GlobalSettings)
  ))
_sym_db.RegisterMessage(GlobalSettings)

GpsSettings = _reflection.GeneratedProtocolMessageType('GpsSettings', (_message.Message,), dict(
  DESCRIPTOR = _GPSSETTINGS,
  __module__ = 'POGOProtos.Settings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.GpsSettings)
  ))
_sym_db.RegisterMessage(GpsSettings)

InventorySettings = _reflection.GeneratedProtocolMessageType('InventorySettings', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYSETTINGS,
  __module__ = 'POGOProtos.Settings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.InventorySettings)
  ))
_sym_db.RegisterMessage(InventorySettings)

LevelSettings = _reflection.GeneratedProtocolMessageType('LevelSettings', (_message.Message,), dict(
  DESCRIPTOR = _LEVELSETTINGS,
  __module__ = 'POGOProtos.Settings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.LevelSettings)
  ))
_sym_db.RegisterMessage(LevelSettings)

MapSettings = _reflection.GeneratedProtocolMessageType('MapSettings', (_message.Message,), dict(
  DESCRIPTOR = _MAPSETTINGS,
  __module__ = 'POGOProtos.Settings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.MapSettings)
  ))
_sym_db.RegisterMessage(MapSettings)

SfidaSettings = _reflection.GeneratedProtocolMessageType('SfidaSettings', (_message.Message,), dict(
  DESCRIPTOR = _SFIDASETTINGS,
  __module__ = 'POGOProtos.Settings_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.SfidaSettings)
  ))
_sym_db.RegisterMessage(SfidaSettings)


# @@protoc_insertion_point(module_scope)