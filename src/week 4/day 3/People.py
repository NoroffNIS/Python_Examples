class People:
    """class-documentation-string """
    name = ''
    age = int()

    count = 0

    def __init__(self, firstname, surename):
        self.name = firstname + ' ' + surename
        People.count += 1

    def display_name(self):
        print('This is my name:', self.name)


    def display_age(self):
        print('This is my age:', self.age)

    def __del__(self):
        print(self.name,' was removed!')

