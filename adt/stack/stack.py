# Create a stack object that has the push, pop, isEmpty methods
# Add 3 new methods
# List all items
# Find item
# Add a list to stack

class Stack:
    # create stack object
    def __init__(self):
         self.items = []

    def isEmpty(self):
         return self.items == []

    def push(self, item):
         self.items.append(item)

    def pop(self):
         return self.items.pop()

    def peek(self):
         return self.items[len(self.items)-1]

    def size(self):
         return len(self.items)

    # Questions the IB will ask you to do     
    def stacky_boy(self):
        for x in self.items:
            print(x)

    def add_to_stacky_boy(self, list):
        for x in list:
            self.push(x)
        print(self.items)
        
    def find_me(self, missing):
        for x in self.items:
            if x == missing:
                print(x)



# init data structure
s = Stack()
# add items to stack
s.push('I')
s.push('really')
s.push('love')
s.push('Shibers')
# remove item from stack
spop = str(s.pop())
print('Popping out %s'%(spop) )
print(s)
s.push('Shibers')
# test our algorithms
s.stacky_boy()
s.add_to_stacky_boy(['meow', 'woof'])
s.find_me('woof')




