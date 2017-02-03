import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32' : base = 'Win32GUI'

opts = { 'include_files' : ['noroff-logo.gif'], 'includes' : [ 'tkinter' ] }

setup(
    name = 'Noroff Images' ,
    version = '1.0' ,
    description = 'Noroff images' ,
    author = 'Brage' ,
    options = {'build_exe' : opts } ,
    executables = [ Executable( 'images.py' , base = base ) ] )