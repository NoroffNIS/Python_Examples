global_var = 2

def add():
    global local_var
    local_var = 2
    global global_var
    print(local_var + global_var)
    global_var = 4

add()
print(global_var + local_var)