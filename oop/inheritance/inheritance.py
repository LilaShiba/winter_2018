class Dog():
    def __init__(self):
        self.bork = 'bork'

class Shiba(Dog):
    def __init__(self):
        super().__init__()
        self.sass = 1000


estelle = Shiba()
print(estelle.bork)
print(estelle.sass)

# OR
class Dog():
    def __init__(self):
        self.bork = 'bork'

class Shiba(Dog):
    sass = 1000


estelle = Shiba()
print(estelle.bork)
print(estelle.sass)
