import random
class Pokemon(object):
	
	def __init__(self,name,hp,type):
		self.name = name
		self.hp = hp
		# define each pokemon type & assign hash table
		if type == 'electric':
			self.type = {
			'1 tackle': random.randint(5, 10),
			'2 shockwave': random.randint(5, 10),
			'3 thunderbolt': random.randint(5, 30),
			'heal': random.randint(-10, -2),
			'para': 0,
			'evolve': 1
			}
		elif type == 'fire':
			self.type = {
			'1 tackle': random.randint(5, 10),
			'2 flame': random.randint(5, 20),
			'3 thrower': random.randint(10, 20),
			'heal': random.randint(-10, -2),
			'para': 0,
			'evolve': 1
			}
		elif type == 'water':
			self.type = {
			'2lvl hydro pump': random.randint(5, 20),
			'hydro vortex': random.randint(10, 20),
			'tackle': random.randint(5, 10),
			'heal': random.randint(-10, -2),
			'para': 0,
			'evolve': 1
			}
		elif type == 'ghost':
			self.type = {
			'shadow ball': random.randint(5, 20),
			'phantom force': random.randint(10, 20),
			'tackle': random.randint(5, 10),
			'heal': random.randint(-10, -2),
			'para': 0,
			'evolve': 1
			}
		elif type == 'psychic':
			self.type = {
			'dream eater': random.randint(5, 20),
			'cosmic power': random.randint(10, 20),
			'confusion': random.randint(5, 10),
			'heal': random.randint(-10, -2),
			'para': 0,
			'evolve': 1
			}
	
	def battle(self, enemy):
		# go over attack choices for each instance
		print("It is %s's turn to attack"%(self.name))
		for x in self.type:
			print(x)
		# Pick attack
		attack_choice = input('what attack do you pick?')
		attack_chossen = self.type[attack_choice]
		
		# Paralyze
		if(self.hp > 1 and attack_chossen == self.type['para']):
			x = random.randint(0,10)
			# 50/50 chance of working
			# If it works skip enemy turn
			if x % 2 == 0:
				print("%s is paralyzed"%(enemy.name))
				self.hp = self.hp + 5
				print("%s now has %d"%(self.name, self.hp))
				if(enemy.hp > 1):
					return self.battle(enemy)
			# If it doesn't work, harm self
			else:
				print("It didn't work")
				self.hp = self.hp - 2
				print("You hurt your self by 2 hp. You now have %s"%(self.hp))
				return enemy.battle(self)
		# Evolve Pokemon!
		elif(self.hp > 1 and attack_choice == 'evolve'):
			if(self.hp > 15):
				self.type.update({'laser': random.randint(15, 30)})
				print("%s is evovling!"%(self.name))
				enemy.hp = enemy.hp + 10
				print("%s toughend their defense!"%(enemy.name))
				return enemy.battle(self)
			else:
				print('You do not have enough HP to evolve')
		# Determine if attack or heal to apply points accordingly
		elif(self.hp > 1 and attack_chossen != self.type['heal']):
			for x, y in self.type.items():
				#update value
				# speed example
				if(x[0] == '1'):
					self.type.update({x: random.randint(5,10)})
				elif(x[0] =='2'):
					self.type.update({x: random.randint(8,15)})
				elif(x[0] =='3'):
					self.type.update({x: random.randint(10,20)})
			enemy.hp -= attack_chossen
			print("")
			print("%s did %d Damage to %s"%(self.name, attack_chossen, enemy.name)) #Text-based combat descriptors
			print("%s has %d HP left"%(enemy.name,enemy.hp)) #Text-based descriptor for the opponent's health
			print(" ")
			if(enemy.hp > 1):
				return enemy.battle(self)
		# Heal Limit
		elif(self.hp >= 20 and attack_chossen == self.type['heal']):
			print('You are already healed!')
			return enemy.battle(self)
		# Heal Self
		elif(self.hp > 1 and attack_chossen == self.type['heal']):
			self.hp -= attack_chossen
			print("")
			print("%s healed %d amount "%(self.name, attack_chossen))
			print("%s has %d HP left"%(self.name,self.hp))
			print("")
			return enemy.battle(self)
		# Win Statement
		else:
			print("%s wins! (%d HP left)" %(enemy.name, enemy.hp)) #declares the winner of the Battle
			return enemy, self  #return a tuple (Winner, Loser)


estelle = Pokemon('estelle', 25, 'electric')
ben = Pokemon('ben', 25, 'fire')
Pokemon.battle(estelle,ben)
