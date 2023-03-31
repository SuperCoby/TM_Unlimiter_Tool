import bpy
import os
import bpy.utils.previews
from bpy.props import EnumProperty, StringProperty
from .. import addon_prefs


PREVIEW_COLLECTIONS = {}
CACHED_TEXTURE_ITEMS = {}


def get_texture_dir_path(ty=None):
    ty = ty or bpy.context.scene.tm_material_type
    return getattr(addon_prefs(), f"{ty.lower()}_path")


def get_image_path(ty=None):
    ty = ty or bpy.context.scene.tm_material_type
    folder = get_texture_dir_path(ty)
    image_name = getattr(bpy.context.scene, f'tm_{ty.lower()}_texture')

    if not folder or not image_name:
        return ''

    return os.path.join(folder, image_name)


# Refresh cached list of texture items
def refresh(ty=None):
    ty = ty or bpy.context.scene.tm_material_type
    folder = get_texture_dir_path(ty)

    items = []
    CACHED_TEXTURE_ITEMS[ty] = items

    for i, fn in enumerate(os.listdir(folder)):
        ident = fn
        name = fn
        description = ""
        icon = load_preview_icon(os.path.join(folder, fn), ty)
        items.append((ident, name, description, icon, i))


# Refresh a texture list if it's not in the cache
def auto_refresh(ty=None):
    ty = ty or bpy.context.scene.tm_material_type
    if ty in CACHED_TEXTURE_ITEMS:
        return
    try:
        refresh(ty)
    except Exception as e:
        pass


# Callback run when a texture path preference changed
def on_texture_path_changed(ty):
    global PREVIEW_COLLECTIONS
    global CACHED_TEXTURE_ITEMS

    del CACHED_TEXTURE_ITEMS[ty]
    if ty in PREVIEW_COLLECTIONS:
        bpy.utils.previews.remove(PREVIEW_COLLECTIONS[ty])
        del PREVIEW_COLLECTIONS[ty]


def fetch_texture_items(ty):
    items = CACHED_TEXTURE_ITEMS.get(ty, [])
    filter = bpy.context.scene.tm_texture_filter

    if filter:
        filter = filter.lower()
        items = [item for item in items if filter in item[0].lower()]

    return items


def fetch_texture_items_tmnf(self, context):
    return fetch_texture_items('TMNF')

def fetch_texture_items_tm2(self, context):
    return fetch_texture_items('TM2')

def fetch_texture_items_tm20(self, context):
    return fetch_texture_items('TM20')


def load_preview_icon(path, ty=None):
    ty = ty or bpy.context.scene.tm_material_type

    pcol = PREVIEW_COLLECTIONS.get(ty)
    if pcol is None:
        pcol = PREVIEW_COLLECTIONS[ty] = bpy.utils.previews.new()

    if not path in pcol:
        try:
            pcol.load(path, path, "IMAGE")
        except Exception:
            return 0

    return pcol[path].icon_id


def create_material(name):
    bpy.ops.object.material_slot_add('INVOKE_DEFAULT')

    material = bpy.data.materials.new(name=name)
    material.use_nodes = True

    slot_index = bpy.context.view_layer.objects.active.active_material_index
    bpy.context.active_object.material_slots[slot_index].material = material

    return material


def add_texture_to_material(material, img_path):
    node_tree = material.node_tree

    img_node = node_tree.nodes.new(type='ShaderNodeTexImage')
    img_node.image = bpy.data.images.load(
        filepath=img_path,
        check_existing=True,
    )

    for node in node_tree.nodes:
        if node.type == 'BSDF_PRINCIPLED':
            node_tree.links.new(img_node.outputs['Color'], node.inputs['Base Color'])
            img_node.location = node.location[0] - 350, node.location[1] - 50
            break


# Refresh cached list of textures.
class SNA_OT_Refresh(bpy.types.Operator):
    bl_idname = "sna.refresh"
    bl_label = "Refresh"
    bl_description = "Refresh TM texture list"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        if not get_texture_dir_path():
            cls.poll_message_set('No texture path set')
            return False

        return True

    def execute(self, context):
        try:
            refresh()
            return {"FINISHED"}
        except Exception as e:
            print(e)
            self.report({'ERROR'}, "Couldn't load textures; check path")
            return {"CANCELLED"}


class SNA_OT_AddTexture(bpy.types.Operator):
    bl_idname = "sna.add_texture"
    bl_label = "Add Texture"
    bl_description = "Add texture to current material"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if not bpy.context.object:
            cls.poll_message_set('No active object')
            return False

        if (
            not bpy.context.object.active_material or
            not bpy.context.object.active_material.node_tree
        ):
            cls.poll_message_set('No active material to add to')
            return False

        return True

    def execute(self, context):
        add_texture_to_material(
            bpy.context.object.active_material,
            get_image_path(),
        )
        return {"FINISHED"}


class SNA_OT_AddTextureMaterial(bpy.types.Operator):
    bl_idname = "sna.add_texture_material"
    bl_label = "Add Texture Material"
    bl_description = "Create new material with current texture"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if not bpy.context.object:
            cls.poll_message_set('No active object')
            return False

        return True

    def execute(self, context):
        img_path = get_image_path()
        if not img_path:
            return {'CANCELLED'}

        mat = create_material(os.path.basename(img_path))
        add_texture_to_material(mat, img_path)
        return {"FINISHED"}


classes = (
    SNA_OT_Refresh,
    SNA_OT_AddTexture,
    SNA_OT_AddTextureMaterial,
)


scene_props = (
    ("tm_material_type", EnumProperty(
        name='TrackMania Material Type',
        items=[
            ('TMNF', 'TMNF', 'TrackMania Nations Forever'),
            ('TM2', 'TM²', 'TrackMania²'),
            ('TM20', 'TM20', 'TrackMania 2020'),
        ],
    )),
    ("tm_tmnf_texture", EnumProperty(
        name='TMNF Texture',
        items=fetch_texture_items_tmnf,
    )),
    ("tm_tm2_texture", EnumProperty(
        name='TM² Texture',
        items=fetch_texture_items_tm2,
    )),
    ("tm_tm20_texture", EnumProperty(
        name='TM20 Texture',
        items=fetch_texture_items_tm20,
    )),
    ("tm_texture_filter", StringProperty(
        name='Filter',
        description='Filter textures by names'
    )),
)


def unregister():
    global PREVIEW_COLLECTIONS
    global CACHED_TEXTURE_ITEMS

    for pcol in PREVIEW_COLLECTIONS.values():
        bpy.utils.previews.remove(pcol)

    PREVIEW_COLLECTIONS = {}
    CACHED_TEXTURE_ITEMS = {}
