from player import *

class Man(Player):
    def action(self, msg_action):
        print(self.name, '\n\t Man player action', msg_action)


class Woman(Player):
    def action(self, msg_action):
        print(self.name, '\n\t Woman player action', msg_action)

man = Man('Jon')
woman = Woman('Kari')

man.action('Kicks the ball in the goal!')
woman.action('Trows the ball in the goal!')

def describe(object):
    object.info()

describe(man)
describe(woman)