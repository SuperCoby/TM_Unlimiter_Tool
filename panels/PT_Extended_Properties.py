import bpy


class VIEW3D_PT_extended_properties(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_extended_properties"
    bl_label = "Extended Properties"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "TM"
    bl_parent_id = "SNA_PT_main"
    bl_order = 50
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        col = layout.column()
        row = col.row()
        row.prop(context.scene, 'gbx_mat_cat')
        if context.scene.gbx_mat_cat == 'Stadium':
            row = col.row()
            row.prop(context.scene, 'gbx_mat_stad')
        if context.scene.gbx_mat_cat == 'Island':
            row = col.row()
            row.prop(context.scene, 'gbx_mat_island')
        if context.scene.gbx_mat_cat == 'Speed':
            row = col.row()
            row.prop(context.scene, 'gbx_mat_speed')
        if context.scene.gbx_mat_cat == 'Rally':
            row = col.row()
            row.prop(context.scene, 'gbx_mat_rally')
        if context.scene.gbx_mat_cat == 'Alpine':
            row = col.row()
            row.prop(context.scene, 'gbx_mat_alpine')
        if context.scene.gbx_mat_cat == 'Coast':
            row = col.row()
            row.prop(context.scene, 'gbx_mat_coast')
        if context.scene.gbx_mat_cat == 'Bay':
            row = col.row()
            row.prop(context.scene, 'gbx_mat_bay')
        if context.scene.gbx_mat_cat == 'Collision':
            row = col.row()
            row.prop(context.scene, 'gbx_mat_col')

        row = col.row()
        row.operator('opr.add_custom_property_type', text='Add Property')


classes = (
    VIEW3D_PT_extended_properties,
)
