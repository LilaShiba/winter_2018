import random
class Pokemon():
    def __init__(self, name, hp, attack, type):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.type = type

    def attack_points(self):
        self.attack = random.randint(0, self.attack)
        return self.attack

    def battle(self, other):
        # pick an attack
        current_attack = input('what attack do you pick  tackle or slap')
        # set value based on choice
        if current_attack == 'tackle':
            current_attack = 10 + self.attack_points()
        else:
            current_attack = 5 + self.attack_points()
        # attack on other and change hp
        print(self.name, 'did', current_attack, 'damage to', other.name)
        other.hp = other.hp - current_attack
        # if other is alive, let other attack
        if other.hp > 0:
            print(other.name, 'has', other.hp, ' left')
            # recursive example
            return(other.battle(self))
        # else game is over
        else:
            print(other.name, 'has been defeated')



# Class ends
# instance of pokemon
squirtle = Pokemon('squirtle', 100, 25, 'water')
ben = Pokemon('ben', 100, 25, 'water')
squirtle.battle(ben)
