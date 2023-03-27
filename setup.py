import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter", "PIL", "os", "time", "textwrap"],
    "include_files": [("my_ico.ico", "my_ico.ico")]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="image_compressor",
    version="1.0",
    description="A simple image compressor application",
    options={"build_exe": build_exe_options},
    executables=[Executable("app.py", base=base, icon="my_ico.ico")]
)
