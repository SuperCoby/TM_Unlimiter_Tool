import bpy


def get_view3d_space():
    for area in bpy.context.screen.areas:
        for space in area.spaces:
            if isinstance(space, bpy.types.SpaceView3D):
                return space
    return None


class SNA_PT_Tools(bpy.types.Panel):
    bl_label = 'Tools'
    bl_idname = 'SNA_PT_Tools'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'TM1'
    bl_parent_id = "SNA_PT_main"
    bl_order = 20
    bl_ui_units_x = 0

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        layout.operator('sna.origin', text='Origin', icon_value=618)

        row = layout.row()
        row.prop(
            bpy.context.space_data.overlay,
            'show_face_orientation',
            text='Show Face Orientation',
            icon_value=0,
        )

        layout.operator('mesh.flip_normals', text='Flip Normal', icon_value=548)

        col = layout.column()
        row = col.row()
        row.scale_x = 1.15
        row.scale_y = 1.2
        row.operator('object.shade_smooth', text='', icon_value=127)
        row.operator('object.shade_flat', text='', icon_value=288)

        row.separator(factor=1.45)

        if bpy.context.active_object and bpy.context.active_object.type == 'MESH':
            mesh = bpy.context.active_object.data
            row.prop(mesh, 'use_auto_smooth', text='', icon_value=0)
            row.prop(mesh, 'auto_smooth_angle', text='', icon_value=0)

        if space := get_view3d_space():
            layout.prop(space, 'lock_camera', text='Lock Camera to View', icon_value=0)

        row = layout.row()
        row.operator('view3d.object_as_camera', text='', icon_value=168)
        row.operator('view3d.view_selected', text='', icon_value=60)
        row.operator('view3d.view_all', text='', icon_value=59)
        row.operator('screen.region_quadview', text='', icon_value=683)


classes = (
    SNA_PT_Tools,
)
