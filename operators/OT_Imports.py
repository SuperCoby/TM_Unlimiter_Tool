from bpy_extras.io_utils import ExportHelper
from bpy.types import Operator
from ..utils.ItemsImport import import_item_gbx, import_items_gbx_folder


class TM_OT_ImportItem(Operator, ExportHelper):
    bl_idname = "view3d.import_item_gbx"
    bl_label = "Import"
    filename_ext = "."
    use_filter_folder = True

    def execute(self, context):
        err = None
        print(self.filepath)
        if self.filepath.lower().endswith(".item."):
            err = import_item_gbx(self.filepath+"Gbx")
        else:
            import_items_gbx_folder(self.filepath)

        if err:
            show_report_popup("Exporting error!", [err], "ERROR")

        return {'FINISHED'}


classes = (
    TM_OT_ImportItem,
)
