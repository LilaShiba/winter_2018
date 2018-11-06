class Music:
	 MajorKeys = 12


class Strings(Music):
	typeOfWood = 'Tonewood'

class Guitar(Strings):
	def __init__(self):
		self.numberOfStrings = 6
		print(" I have {} strings, I'm made of {}, and can play {} keys ".format(self.numberOfStrings, self.typeOfWood, self.MajorKeys))


guitar = Guitar()