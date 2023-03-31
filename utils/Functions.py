import re
from .Constants import *
from .. import ADDON_ROOT_PATH

def fix_slash(filepath: str) -> str: return filepath
def get_addon_path() -> str: return fix_slash(ADDON_ROOT_PATH + "/")

def get_blendermania_dotnet_path() -> str:
    from .Constants import BLENDER_INSTANCE_IS_DEV
    if BLENDER_INSTANCE_IS_DEV:
        return fr"D:\Art\Blender\blendermania-dotnet\blendermania-dotnet\bin\Release\net7.0\win-x64\publish\blendermania-dotnet.exe"
    else:
        return get_addon_path() + f"utils/{BLENDERMANIA_DOTNET}.exe"

def install_blendermania_dotnet()->None:
    """download and install blendermania-dotnet"""
    tm_props = get_global_props()
    url      = WEBSPACE_DOTNET_EXECUTABLE
    
    tm_props.CB_DL_ProgressShow = True

    extract_to   = get_addon_assets_path()
    file_path    = f"""{extract_to}/{BLENDERMANIA_DOTNET}.zip"""
    progressbar = "NU_DL_Progress"

    def on_success():
        delete_files_by_wildcard(f"{extract_to}/Blendermania_Dotnet*.exe")

        tm_props.CB_DL_ProgressRunning = False
        unzip_file_into(file_path, extract_to)
        def run(): 
            tm_props.CB_DL_ProgressShow = False
        timer(run, 5)
        debug(f"downloading & installing blendermania-dotnet {get_global_props().LI_gameType} successful")
        os.remove(file_path)

    def on_error(msg):
        tm_props.ST_DL_ProgressErrors = msg or "unknown error"
        tm_props.CB_DL_ProgressRunning = False
        debug(f"downloading & installing blendermania-dotnet {get_global_props().LI_gameType} failed, error: {msg}")

    create_folder_if_necessary(extract_to)
    debug(f"try to download & install blendermania-dotnet")

    print(url)
    download = DownloadTMFile(url, file_path, progressbar, on_success, on_error)
    download.start()
    tm_props.NU_DL_Progress        = 0
    tm_props.ST_DL_ProgressErrors  = ""
    tm_props.CB_DL_ProgressRunning = True

    #loop over viewlayer (collection->children) <-recursive until obj col[0] found
    for hierachy_col in hierachy: #hierachy collection
        
        #set first collection
        if current_col == "": 
            current_col = view_layer.layer_collection.children[hierachy_col]
        
        else:
            current_col = current_col.children[hierachy_col]
            
        if current_col.name == col.name: #last collection found

            if current_col.exclude or current_col.is_visible is False:
                collection_is_excluded = True # any col in hierachy is not visible or enabled, ignore this col.
                break
            

    return True if collection_is_excluded else False

def get_abs_path(path: str):
    return os.path.abspath(path) if path else ""

def get_global_props() -> object:
    return bpy.context.scene.tm_props
    
def ireplace(old, new, text):
    idx = 0
    while idx < len(text):
        index_l = text.lower().find(old.lower(), idx)
        if index_l == -1:
            return text
        text = text[:index_l] + new + text[index_l + len(old):]
        idx = index_l + len(new) 
    return text
    
    

