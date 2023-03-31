import bpy


# Main sidebar panel to parent others to
class SNA_PT_main(bpy.types.Panel):
    bl_label = "Main"
    bl_idname = "SNA_PT_main"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "TM"

    def draw(self, context):
        layout = self.layout


classes = (
    SNA_PT_main,
)
