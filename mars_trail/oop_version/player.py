import random
import kessel_run

class Player:

    def __init__(self, hp, name):
        self.hp = hp
        self.name = name

    def alive(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def heal(self):
        heal_amount = random.randint(0,10)
        print('you healed', heal_amount)
        self.hp += heal_amount
        print('your hp is now', self.hp)
        return self.hp



class Ship():

    def __init__(self, hp, mass, energy, cache, players):
        self.hp = hp
        self.mass = mass
        self.energy = energy
        self.cache = cache
        self.players = players

    def flip_and_burn(self, distance):
        pass

    def alive(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def battle(self, other):
        print(self.players.name, 'and', other.players.name, 'are battleing')
        # continue while both are alive
        while self.alive() and other.alive():
            # print info
            self.weapons_info()
            # get choice
            next_move = input('do you heal, fight, run away, escape pod? (h/f/r/e)')
            # add attack damage
            if next_move == 'f':
                attack_choice = input('what attack do you pick?\n')
                attack_chossen = self.cache[attack_choice]
                other.hp = other.hp - attack_chossen
                print(other.players.name, 'ship has', other.hp, 'hp left\n')
            # heal
            elif next_move == 'h':
                self.players.heal()
            # escape pod
            elif next_move == 'e':

            # run away through an asteroid belt
            #else:
            #    distance = random.randint(10000,10000000000)
            #    print('you must travel', distance, 'to get to safety')
            #    print('there is an asteroid belt. Maybe you will make it')
            #    self.players.flip_and_burn()
            # continue if both players are alive
            if other.hp > 0:
                return other.battle(self)

            print(other.players.name, 'has been defeated!')

    def info(self):
        print('hp is at', self.hp)
        print('your ship has a mass of', self.mass)
        print('your energy is', self.energy)
        print(self.players.name, 'is on the ship with', self.players.hp, 'hp left')

    def weapons_info(self):
        for x,y in self.cache.items():
            print('your cache has', y, x)


estelle = Player(100, 'Estelle')
meowmeow = Player(100, 'Meowmeow')
ross = Ship(1000,10000,5000,{'lasers': 10000},estelle)
boss = Ship(1000,10000,5000,{'lasers': 10},meowmeow)
ross.info()
ross.battle(boss)
