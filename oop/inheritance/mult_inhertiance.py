class OperatingSystem:
	multitasking = True
	name = "Mac OS"

class Apple:
	website='www.apple.com'
	name = "Apple"

class MacBook(OperatingSystem, Apple):
	def __init__(self):
		if self.multitasking is True:
			print('This multitasking systems is great. Visit {} for more info'.format(self.website))
			print(self.name)
mac = MacBook()

