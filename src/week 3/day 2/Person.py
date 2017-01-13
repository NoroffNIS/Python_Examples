name = ''
age = 0
address = ''
zipcode = 0

def print_name(name_in='NAME'):
    global name
    name = name_in
    print('This is the name', name)

def display_age():
    print('This is the age:', age)

def display_address():
    print(name,'\n',address,'\n', zipcode)

def get_age():
    return age

def set_age(a):
    global age
    age = a