import random
class Pokemon(object):
	
	def __init__(self,name,hp,type):
		self.name = name
		self.hp = hp
		# define each pokemon type with control flow
		if type == 'electric':
			self.type = {
				'shock': random.randint(10,15),
				'thunderbolt': random.randint(15,20),
				'heal': random.randint(-5, -1)

			}
		elif type == 'fire':
			self.type = {
				'fire': random.randint(10,15),
				'thrower': random.randint(15,20)
			}
		else:
			print('not a choice')

	# random attack value doesn't work for each attack
	def battle(self, enemy):
		# go over attack choices for each instance
		for x in self.type:
			print(x)

		# Note to user who is attacking?
		print("%s turn to attack %s"%(self.name, enemy.name))	
		# Get user Input
		user_choice = input('what attack you want brah?')
		# Use user Input to apply attack to enemy
		chossen_attack = self.type[user_choice]
		# Attack while HP > 1
		if(self.hp > 1):
			# Loop to update values of self.type
			for x, y in self.type.items():
				# update value
				# speed example 
				if(x == 'fire'):
					self.type['fire'] = random.randint(10,15)
				elif(x =='thrower'):
					self.type['thrower'] = random.randint(10,20)
				elif(x =='thunderbolt'):
					self.type['thunderbolt'] = x: random.randint(10,20)
				elif(x == 'shock'):
					self.type['shock']x: random.randint(10,15)
			#
			#
			print(self.type)
			enemy.hp = enemy.hp - chossen_attack
			print("%s did %d damge to %s"%(self.name,chossen_attack, enemy.name))
			print("%s has %d HP left"%(enemy.name, enemy.hp))
			if (enemy.hp > 1):
				return enemy.battle(self)
			# End battle if HP < 1
			elif(enemy.hp < 1):
				print("%s is knocked out %s won"%(enemy.name, self.name))
		


# Running the game / init your class & call methods
estelle = Pokemon('estelle', 25, 'electric')
ben = Pokemon('ben', 25, 'fire')
Pokemon.battle(estelle,ben)
