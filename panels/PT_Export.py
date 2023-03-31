import bpy


class GBX_PT_Export(bpy.types.Panel):
    bl_idname = 'GBX_PT_Export'
    bl_label = 'GBX Exporter'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "TM"
    bl_parent_id = "SNA_PT_main"
    bl_order = 40

    def draw(self, context):
        col = self.layout.column()

        col.prop(context.scene, 'gbx_author')
        col.prop(context.scene, 'gbx_spawn_x')
        col.prop(context.scene, 'gbx_spawn_y')
        col.prop(context.scene, 'gbx_spawn_z')
        col.prop(context.scene, 'gbx_exp_dir')

        col.operator('opr.gbx_export_batch', text='Export')


classes = (
    GBX_PT_Export,
)
