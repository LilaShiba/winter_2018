import random
class Pokemon():

    def __init__(self, hp, name):
        self.hp = hp
        self.name = name

    def battle(self, other):
        print(self.name, 'is in a fight with', other.name)
        # get user input for an attack
        pick_attack = input('what attack? slap or tackle')
        # basic if/else
        if pick_attack == 'slap':
            attack = random.randint(5,25)
        else:
            attack = random.randint(0,50)
        # subtract other.hp
        other.hp = other.hp - attack
        # see hp as battle moves on
        print(self.name, 'did', attack, 'damage to', other.name)
        print(other.name, 'has', other.hp, 'health left\n')
        # check if other is not knocked out
        if other.hp > 0:
            return(other.battle(self))
        else:
            print(self.name, 'won')




# create an instance of the class
pablo = Pokemon(100, 'pablo')
teddy = Pokemon(100, 'teddy')
pablo.battle(teddy)
