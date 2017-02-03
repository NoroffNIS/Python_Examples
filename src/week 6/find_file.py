import sys, os

def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
        print(datadir)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)
        print(datadir)
    return os.path.join(datadir, filename)


path = 'C:\\Users\\noro-bro\\AppData\\Local\\slack\\app-2.4.1\\resources\\app.asar.unpacked\\node_modules\edge-atom-shell\\build\Release\\'

def get_dll(path):
    dllfiles = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith('.dll'):
                dllfiles.append(path+'\\'+name)
            else:
                print(name)
    return dllfiles

