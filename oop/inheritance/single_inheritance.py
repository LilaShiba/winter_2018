class Apple:
	manufacturer = 'Apple Inc'
	contactWebsite = "www.apple.com/contact"

	def contactDetails(self):
		print('to contact us log on to ' + self.contactWebsite)


class MacBook(Apple): 
#inherits from class Apple
# Apple is the base class
# Mac is the derived class

	def __init__(self):
		self.yearOfManufacture = 2017

	def manufactureDetails(self):
		print("This mac was manufactured in year {} by {}".format(self.yearOfManufacture, self.manufacturer))


mac = MacBook()
mac.manufactureDetails()
mac.contactDetails()