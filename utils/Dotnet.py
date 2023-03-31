import json
import subprocess
from .Constants      import *
from .Functions      import *

class DotnetExecResult:
    success: bool
    message: str
    def __init__(self, message: str, success: bool):
        self.success = success
        self.message = message

class DotnetConvertItemToObj:
    def __init__(
        self,
        ItemPath: str,
        OutputDir: str,
    ):
        self.ItemPath = ItemPath
        self.OutputDir = OutputDir

    def jsonable(self):
        return self.__dict__

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'jsonable'):
            return obj.jsonable()
        else:
            return json.JSONEncoder.default(self, obj)

def run_convert_item_to_obj(
    item_path: str,
    output_dir: str,
) -> DotnetExecResult:
    config_path = fix_slash(os.path.dirname(get_abs_path(item_path)))+'/convert-item.json'
    with open(config_path, 'w+', encoding='utf-8') as outfile:
        json.dump(DotnetConvertItemToObj(item_path, output_dir), outfile, cls=ComplexEncoder, ensure_ascii=False, indent=4)
        outfile.close()

        res = _run_dotnet(CONVERT_ITEM_TO_OBJ, config_path)
        res.message = res.message.replace("SUCCESS: ", "")
        print(res)
        if not BLENDER_INSTANCE_IS_DEV:
            try:
                os.remove(config_path)
            except FileNotFoundError:
                pass
        return res

def _run_dotnet(command: str, payload: str) -> DotnetExecResult:
    #print(payload)
    dotnet_exe = get_blendermania_dotnet_path()

    process = subprocess.Popen(args=[
        dotnet_exe,
        command,
        payload.strip('"'),
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    out, err = process.communicate()
    if len(err) != 0:
        return DotnetExecResult(message=err.decode("utf-8") , success=False)
    
    res = out.decode("utf-8").strip()
    if process.returncode != 0:
        return DotnetExecResult(message="Unknown Error", success=False) if len(res) == 0 else res

    return DotnetExecResult(message=res, success=True)