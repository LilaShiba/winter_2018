import random, requests, bs4

class Planets(object):

	def __init__(self, name, grade, book_history):
		self.name = name
		self.grade = grade
		self.book_history = book_history
		self.types = {}

	def show_books(self):
		for x in self.book_history:
			print(x)
		print("")

	def organize_books(self, friend):
		# find what books are common
		shared_books = [element for element in self.book_history if element in friend.book_history]
		shared_books = str(shared_books)[1:-1]
		print("%s and %s have %s in common"%(self.name, friend.name, shared_books))

	def add_book(self):
		add_what_book = input('type what book would you like to add')
		# what data structure for book_history?
		# right now it's an array
		self.book_history.append(add_what_book)

	def remove_book(self):
		remove_what_book = input('what book would you like to remove')
		if remove_what_book in self.book_history:
			self.book_history.remove(remove_what_book)
		else:
			print('Book not in history')
			show_books(self)
			remove_book(self)

meow = Planets('Estelle', 1000, ['woof', 'for whom the dog borks', 'where are my keys'])
woof = Planets('Ben', 1000, ['hay hay', 'where is my carrot', 'woof'] )
bork = Planets('Catto', 10000, ['meow', 'meow vs. bork', 'where is my carrort'])

all_users = [meow, woof, bork]
while True:
	print(" 1 show books, 2 add books, 3 remove books, 4, find friends, 5 exit")
	print("")
	userChoice = int(input())
	if userChoice is 1:
		meow.show_books()
	elif userChoice is 2:
		meow.add_book()
	elif userChoice is 3:
		meow.remove_book()
	elif userChoice is 4:
		Planets.organize_books(meow, bork)
	else:
		exit()
		