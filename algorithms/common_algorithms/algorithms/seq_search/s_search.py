# Create a stack object that has the 
# push, pop, isEmpty methods
class Stack:
# init  !!!
	def __init__(self):
		self.items = []
# create a push method
# inherient self, and user gives us data
	def push(self, item):
		self.items.append(item)
# create a pop method
# taking in self, and user does not say what to pop
# because stack is LIFO
	def pop(self):
		self.items.pop()
# return a boolean
	def isEmpty(self):
		a = []
		if self.items == a:
			# print for debugging
			print('True')
			return True
		else:
			print('False')
			return False

	# Add 3 new methods
	
	# List all items
	# for vs. while
	def list_items(self):
		for x in self.items:
			print(x)


	# Sequential Search  		
	def s_search(self, missing):
		for x in range(len(self.items)):
			if self.items[x] == missing:
				print(x)


	# bubble sort
	def b_sort(self):
		# get length of stack
		n = len(self.items)
		for x in range(n):
			for y in range(0,n-x-1):
				# Compare size of number by calling index
				if self.items[y] > self.items[y+1]:
					# Swap numbers
					self.items[y], self.items[y + 1] = self.items[y + 1], self.items[y]
		print(self.items)

# create a new stack
dog_stack = Stack()
cat_stack = Stack()
# populate some data
dog_stack.push(100)
dog_stack.push(1)
dog_stack.push(10)
# Test to see if empty
dog_stack.isEmpty()
# Test bubble sort
dog_stack.b_sort()
dog_stack.s_search(10)