import bpy
import math
import os
from pathlib import Path
from .Constants import WAYPOINTS
from .Functions import (ireplace)
from .Dotnet import run_convert_item_to_obj
from .BlenderObjects import create_collection_in, move_obj_to_coll

def import_items_gbx_folder(folder_path: str):
    folder_path = fix_slash(folder_path)
    parts = folder_path.split("/")
    base_coll = create_collection_in(bpy.context.collection, parts[len(parts) - 2])
    for item_path in glob.iglob(folder_path + '**/*.gbx', recursive=True):
        item_path = fix_slash(item_path)
        if not item_path.lower().endswith("gbx"):
            continue

        name = Path(item_path).stem
        name = ireplace(".item", "", name)

        path = item_path.replace(folder_path, "")
        coll = base_coll
        for part in path.split("/"):
            if part.lower().endswith(".gbx"):
                break

            new_name = coll.name+"_"+part
            if new_name in coll.children:
                coll = coll.children[new_name]
            else:
                coll = create_collection_in(coll, new_name)
        
        import_item_gbx(item_path, name, coll)

def import_item_gbx(item_path: str, name: str = None, coll: bpy.types.Collection = None):
    if coll == None:
        coll = bpy.context.collection

    if name == None:
        name = Path(item_path).stem
        name = ireplace(".item", "", name)


    output_dir = os.path.dirname(item_path)

    res = run_convert_item_to_obj(item_path, output_dir)
    if not res.success:
        return res.message

    bpy.ops.import_scene.obj(filepath=res.message)
    objs = bpy.context.selected_objects
    _clean_up_imported_item_gbx(objs, name, coll)

    os.remove(res.message)

    return None

def _clean_up_imported_item_gbx(objs: list[bpy.types.Object], item_name: str, dest_coll: bpy.types.Collection):
    coll = create_collection_in(dest_coll, item_name)

    for obj in objs:
        obj:bpy.types.Object = obj
        move_obj_to_coll(obj, coll)
        obj.name = f"{item_name} {obj.name}"

        

        # fix UV
        if len(obj.data.uv_layers) > 0:
            obj.data.uv_layers[0].name = "BaseMaterial"

        # auto smooth
        obj.data.polygons.foreach_set('use_smooth',  [True] * len(obj.data.polygons))
        obj.data.use_auto_smooth = 1
        obj.data.auto_smooth_angle = math.pi/6  # 45 degrees

    return None