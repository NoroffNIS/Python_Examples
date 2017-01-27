class Player:
    count = 0
    firstname = ''
    surename = ''
    name = firstname + surename
    gender = ''
    shirt_number = int()
    position = 'No position'

    def __init__(self, name):
        self.name = name
        Player.count += 1

    def info(self):
        print(self.name,
              '\n\tGender:', self.gender,
              '\n\tShirt Number:', self.shirt_number,
              '\n\tPosition:', self.position)

    def action(self, msg_action='Default action'):
        print(self.name, '\n\t', msg_action)
