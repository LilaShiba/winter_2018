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
         print(self.items)

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
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# init data structure
s = Stack()
# add items to stack
s.push('I')
s.push('really')
s.push('love')
s.push('Shibers')
s.pop()
s.peek()
