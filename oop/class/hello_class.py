import random


class MyClass(object):

    def dothis(self):
        self.rand_val = random.randint(1, 100)


myInst = MyClass()
myInst.dothis()
print(myInst.rand_val)