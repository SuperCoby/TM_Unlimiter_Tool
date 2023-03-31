import os

DOTNET_COMMANDS = (CONVERT_ITEM_TO_OBJ := "convert-item-to-obj")
ICON_IMPORT             = "IMPORT"
BLENDERMANIA_DOTNET = "Blendermania_Dotnet_v0.0.5"

class WaypointDict(dict):""""""

WAYPOINT_VALID_NAMES = ()
WAYPOINT_NAME_NONE = "None"
WAYPOINTS = WaypointDict()

PANEL_CLASS_COMMON_DEFAULT_PROPS = {
    "bl_category":       "Blendermania",
    "bl_space_type":     "VIEW_3D",
    "bl_region_type":    "UI",
    "bl_options":        {"DEFAULT_CLOSED"}
}

from .Functions import (get_addon_path)
BLENDER_INSTANCE_IS_DEV = os.path.exists(get_addon_path() + ".git")
