class A:
	# Base class and method
	def method(self):
		print('this method is from class A')

class B(A):
	# Override base class
	def method(self):
		print("this method is from class B")

class C(A):
	# Override base class
	def method(self):
		print("this method is from class C")

class D(B, C):
	# Out put depends on order of inheritence
	# Hence b is first, so it will output B
	pass

d = D()
d.method()