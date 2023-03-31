import bpy
from .. import addon_prefs
from ..operators.OT_Materials import auto_refresh


class SNA_PT_Materials(bpy.types.Panel):
    bl_label = 'Materials'
    bl_idname = 'SNA_PT_Materials'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'TM'
    bl_order = 30
    bl_ui_units_x=0
    bl_parent_id = "SNA_PT_main"

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout

        # Automatically refresh the texture list when this panel becomes
        # visible if it hasn't been refreshed yet
        auto_refresh()

        layout.prop(
            bpy.context.scene,
            'tm_material_type',
            text=bpy.context.scene.tm_material_type,
            expand=True,
        )

        layout.operator('sna.refresh', text='Refresh')
        layout.prop(
            addon_prefs(),
            f'{bpy.context.scene.tm_material_type.lower()}_path',
            text='',
        )

        layout.template_icon_view(
            bpy.context.scene,
            f'tm_{bpy.context.scene.tm_material_type.lower()}_texture',
            show_labels=True,
            scale=5.0,
            scale_popup=5.0,
        )
        layout.prop(bpy.context.scene, 'tm_texture_filter', text="Filter")

        layout.operator('sna.add_texture', text='Add texture to material')
        layout.operator('sna.add_texture_material', text='Create new material and texture')


classes = (
    SNA_PT_Materials,
)
