import bpy
from ..utils.Functions import *
from ..operators.OT_Imports import TM_OT_ImportItem


class TM_PT_Imports(bpy.types.Panel):
    bl_label = "Import"
    locals().update( PANEL_CLASS_COMMON_DEFAULT_PROPS )
    bl_parent_id = "SNA_PT_main"
    bl_order = 60

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        col = box.column(align=True)
        row = col.row(align=True)
        row.scale_y = 1.5

        col = box.column(align=True)
        row = col.row()
        row.scale_y = 0.8
        row.label(text="Trackmania:")
        row = col.row()
        row.alert = True
        row.scale_y = 0.7

        row = col.row(align=True)
        row.scale_y = 1.5
        row.operator(TM_OT_ImportItem.bl_idname, text=f"Import .Item.Gbx", icon=ICON_IMPORT)


classes = (
    TM_PT_Imports,
)

