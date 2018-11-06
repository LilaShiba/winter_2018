class Library:
	def __init__(self, listOfBooks):
		self.availableBooks = listOfBooks

	def displayAvailableBooks(self):
		print()
		print('Available Books:')
		for book in self.availableBooks:
			print(book)

	def lendBook(self, requestedBook):
		if requestedBook in self.availableBooks:
			print ("You got it")
			self.availableBooks.remove(requestedBook)
		else:
			print('sorry no book')

	def addBook(self, x):
		self.availableBooks.append(x)
		print("You returned the book!")



class Customer:
	def requestBook(self):
		print('what book you want')
		self.book = input()
		return self.book

	def returnBook(self):
		print('what book to return')
		self.book = input()
		return self.book
		print()

library = Library(['For Whom the Bell Tolls', 'Cat in the Hat', 'Space Stuff'])
customer = Customer()
while True:
	print()
	print()
	print('Enter 1 to display books')
	print('Enter 2 to request book')
	print('Enter 3 to return book')
	print('Enter 4 to exit')
	userChoice = int(input())
	
	# Examples of abstraction & encapsulation
	if userChoice is 1:
		library.displayAvailableBooks()
	elif userChoice is 2:
		requestedBook = customer.requestBook()
		library.lendBook(requestedBook)
	elif userChoice is 3:
		returnedBook = customer.returnBook()
		library.addBook(returnedBook)
	elif userChoice is 4:
		quit()

