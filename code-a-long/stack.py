class Stack():
    # create stack object
    def __init__(self):
        self.items = []

    def isEmpty(self):
        # return a boolean
        return self.items == []

    def push(self, item):
        self.items.append(item)

# create an instance of our class
estelle = Stack()
estelle.push('bork')
print(estelle.isEmpty())

class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

# Instance Queue
q_list = Queue()
