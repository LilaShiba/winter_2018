class Dog():
    def __init__(self, color):
        self.bork = 'bork'
        self.color = 'red'

    def dog_park(self, other):
        print(self.bork, 'and', other.sass)

class Shiba(Dog):
    def __init__(self):
        super().__init__(color)
        self.sass = 1000





estelle = Shiba()
jack = Dog()
print(estelle.bork)
print(estelle.sass)
jack.dog_park(estelle)

# OR
class Dog():
    def __init__(self):
        self.bork = 'bork'

    def dog_park(self, other):
        print(self.bork, 'and', other.sass)


class Shiba(Dog):
    sass = 1000
    zoom = 20000


estelle = Shiba()
print(estelle.bork)
print(estelle.sass)
print(estelle.zoom + 1000)
jack.dog_park(estelle)
