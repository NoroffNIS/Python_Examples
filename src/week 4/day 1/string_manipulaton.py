string_var = 'hello'
name = 'Brage'
ny_tekst = string_var + name
print(ny_tekst)

print(string_var[1])
print(string_var[0:4])

boolean = name not in string_var
print(boolean)

print(string_var,r'\t',name)

def display(s):
    '''Add args, this will print out the arg'''
    print(s)

display(display.__doc__)

print(display.__doc__)