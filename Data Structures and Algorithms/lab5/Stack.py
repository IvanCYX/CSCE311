
## stack implementation using list; replace this one with the implementation using a singly linked list
class Stack():
	def __init__(self):
		self.list=[]

	def push(self, x):
		self.list.append(x)

	def pop(self):
		assert len(self.list) > 0
		temp = self.list[-1]
		del self.list[-1]
		return temp

	def peek(self):
		assert len(self.list) > 0
		return self.list[-1]

	def size(self):
		return len(self.list)

