import random

attack = random.randint(0,100)

class Pokemon():

    def __init__(self, hp, atk, name):
        self.hp = hp
        self.atk = atk
        self.name = name

    def battle(self, other):
        print(self.name, 'and', other.name, 'are fighting')
        # pick an attack
        # get user input for atk
        other.hp = other.hp - # apply user choice
        print(other.name, 'now has', other.hp, 'health left')
        # end condition
        if other.hp > 0:
            return other.battle(self)
        else:
            print(other.name, 'is knocked out')



# pokemon object
izzy = Pokemon(100, 25, 'izzy')
nick = Pokemon(100, 25, 'nick')
izzy.battle(nick)
