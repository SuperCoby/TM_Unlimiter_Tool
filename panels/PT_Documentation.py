import bpy


class SNA_PT_Documentation(bpy.types.Panel):
    bl_label = 'Documentation'
    bl_idname = 'SNA_PT_Documentation'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'TM1'
    bl_parent_id = "SNA_PT_main"
    bl_order = 10
    bl_ui_units_x = 0

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        split = layout.split(factor=0.5, align=False)
        split.operator(
            'sna.open_documentation',
            text='Open Webpage',
        )
        split.operator(
            'sna.open_discord',
            text='Discord',
        )


classes = (
    SNA_PT_Documentation,
)
