import bpy


class SNA_OT_Origin(bpy.types.Operator):
    bl_idname = "sna.origin"
    bl_label = "Origin"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        return {"FINISHED"}


classes = (
    SNA_OT_Origin,
)
