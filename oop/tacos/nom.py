import random
class Taco:
	def __init__(self,taco_type):
		self.menu = taco_type

	def show_menu(self):
		for x in self.menu:
			print(x)

	def get_food(self, requestedFood):
		if requestedFood in self.menu:
			print('Here you go fool')
			self.menu.remove(requestedFood)
		else:
			print('sorry no nom like that')

	def check(self, payment):
		price = str(random.randint(1, 10000))
		print('your price is ' + price+ ' schmeckles')
		self.menu.append(payment)
		# Add a feature to have price tied to food ordered


class Customer:
	def requestFood(self):
		print('what nom you want')
		self.food = input()
		return self.food


	def requestCheck(self):
		print('What did you eat?')
		self.food = input()
		return self.food

taco = Taco(['pizza', 'taco', 'sushi'])
customer = Customer()
while True:
	print(" 1 menu, 2 order, 3 check, 4 exit")
	userChoice = int(input())
	if userChoice is 1:
		taco.show_menu()
	elif userChoice is 2:
		requestedFood = customer.requestFood()
		taco.get_food(requestedFood)
	elif userChoice is 3:
		payment = customer.requestCheck()
		taco.check(payment)
	else:
		exit()
