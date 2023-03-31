import os
import bpy
from bpy.props import *
from bpy.types import Operator
from .. import ADDON_ROOT_PATH


class TM_OT_Items_Edges_Import(Operator):
    """Import a Edge Base"""
    bl_idname = "view3d.tm_importwaypointspawnhelper"
    bl_description = "Import Edge"
    bl_icon = 'MATERIAL'
    bl_label = "Edge Base"
    bl_options = {"REGISTER", "UNDO"}  # without, ctrl+Z == crash

    edges: EnumProperty(items=[
        ("StadiumCircuitBorderStraight", "StadiumCircuitBorderStraight", "", "EDGESEL", 0),
        ("StadiumFabricRamp",     "StadiumFabricRamp",     "", "EDGESEL", 1),
        ("StadiumRoadDirt",       "StadiumRoadDirt",       "", "EDGESEL", 2),
        ("StadiumRoadMainAir",    "StadiumRoadMainAir",    "", "EDGESEL", 3),
        ("StadiumRoadMainGrass",  "StadiumRoadMainGrass",  "", "EDGESEL", 4),
        ("StadiumTrenchStraight", "StadiumTrenchStraight", "", "EDGESEL", 5),
    ])

    def execute(self, context):
        edge = self.properties.edges
        print(ADDON_ROOT_PATH)
        edgePath = os.path.join(ADDON_ROOT_PATH, "assets", "item_edges", f"{edge}.obj")
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.import_scene.obj(filepath=edgePath)

        for obj in bpy.context.selected_objects:
            if "_edge_" in obj.name.lower():
                obj.location = bpy.context.scene.cursor.location

        return {"FINISHED"}

    @staticmethod
    def addMenuPoint_EDGE_SPAWN(self, context):
        layout = self.layout
        layout.operator_menu_enum("view3d.tm_importwaypointspawnhelper", "edges", icon="EDGESEL")


classes = (
    TM_OT_Items_Edges_Import,
)


def register():
    bpy.types.VIEW3D_MT_add.prepend(TM_OT_Items_Edges_Import.addMenuPoint_EDGE_SPAWN)


def unregister():
    bpy.types.VIEW3D_MT_add.remove(TM_OT_Items_Edges_Import.addMenuPoint_EDGE_SPAWN)
