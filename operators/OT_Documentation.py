import bpy
import webbrowser


class SNA_OT_OpenDocumentation(bpy.types.Operator):
    bl_idname = "sna.open_documentation"
    bl_label = "Documentation"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        webbrowser.open('https://docs.google.com/document/d/1NPc3UE9vzHdGh73wqbt_pFpTByCeFQFgEFyGJ88DiCs/edit')
        return {"FINISHED"}


class SNA_OT_OpenDiscord(bpy.types.Operator):
    bl_idname = "sna.open_discord"
    bl_label = "Discord"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        webbrowser.open('https://discord.gg/n8mW58Uq')
        return {"FINISHED"}


classes = (
    SNA_OT_OpenDocumentation,
    SNA_OT_OpenDiscord,
)
