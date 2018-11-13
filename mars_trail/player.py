import random
class Player:

    def __init__(self, hp, job, skill_lvl):
        self.hp = hp
        self.job = job
        self.skill_lvl = skill_lvl

    def skill_growth(self, type, amount):
        self.skill_lvl[type] = amount
        return self.skill_lvl

    def job(self):
        if self.job = 'pilot':
            self.hp = 100
            self.skill_lvl = {}
        elif self.job = 'warrior':
            self.hp = 150
            self.skill_lvl = {}

    def alive(self):
        if self.hp <= 0:
            return False
        else:
            return True



class Ship:

    def __init__(self, hp, mass, energy, cache, players):
        self.hp = hp
        self.mass = mass
        self.energy = energy
        self.cache = cache
        self.players = players
