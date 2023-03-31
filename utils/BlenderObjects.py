import bpy

def move_obj_to_coll(obj: bpy.types.Object, destColl: bpy.types.Collection):
    for coll in obj.users_collection:
        coll.objects.unlink(obj)
    
    destColl.objects.link(obj)

def create_collection_in(destColl: bpy.types.Collection, name: str) -> bpy.types.Collection:
    coll = bpy.context.blend_data.collections.new(name=name)
    destColl.children.link(coll)
    return coll

