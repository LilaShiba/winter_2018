import random, pprint

class SpaceShip:
  population = 0
  ships = []
  def __init__(self, mass, velocity, attack, health, fuel, name):
    self.mass = mass
    self.velocity = velocity
    self.attack = attack
    self.health = health
    self.fuel = fuel
    self.name = name
    SpaceShip.population += 1
    SpaceShip.ships.append([self.name, velocity])


  def power(self):
    power = self.mass * self.velocity
    return power

  def health(self, hit):
    self.health = self.health - hit
    return self.health

  def time_to_travel(self, distance):
    time_to = distance/self.velocity
    time_in_days = time_to/24
    time_in_years = round(time_in_days/365, 2)
    return [time_in_days, time_in_years]
  
  def battle(self, other):
    print(self.name, 'and', other.name, 'are battleing')
    while self.health > 0:
      self.health = self.health - other.attack
      if self.health > 0:
        print(self.name, 'has ', self.health, 'left')
        return other.battle(self)
      else:
        print(self.name, 'is dead')
        print(other.name, 'won')
        other.health = 100000
        other.attack = other.attack * 2
        print(other.name, 'looted your scraps and now has', other.health, 'health and', other.attack,'power attack')
      

  
  @classmethod
  def how_many_ships(meow):
    """Prints the current population."""
    print("We have {:d} ships.".format(meow.population))

  @classmethod 
  def fastest_ship(ship):
    fastest = 0
    for x in ship.ships:
      if x[-1] > fastest:
        fastest = x[-1]
        fast_boy_name = x[0]
    return fast_boy_name, fastest
    

infin = SpaceShip(10000, 300000000, 150, 1500, 100000,'infin')
print(infin.health)
print(infin.power())
print(infin.time_to_travel(25000000000000)[1]
)

nos = SpaceShip(10000, 400000000, 150, 1500, 100000,'nos')
print(nos.time_to_travel(25000000000000)[1])
SpaceShip.how_many_ships()
print(SpaceShip.fastest_ship())

infin.battle(nos)
