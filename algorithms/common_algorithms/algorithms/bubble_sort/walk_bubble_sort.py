
class Stack():

	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		self.items.pop()

	def isEmpty(self):
		a = []
		if self.items == a:
			# print for debugging
			print('True')
			return True
		else:
			print('False')
			return False

	def b_sort(self):
		n = len(self.items)

		for x in range(n):
			for y in range(0, n-x-1):
				if self.items[y] > self.items[y + 1]:
					self.items[y], self.items[y + 1] = self.items[y + 1], self.items[y]

		print(self.items)

	def s_sort(self, )
	

bork = Stack()
bork.push(10)
bork.push(1000)
bork.push(100)
bork.push(20)
bork.push(200)

bork.isEmpty()
bork.b_sort()