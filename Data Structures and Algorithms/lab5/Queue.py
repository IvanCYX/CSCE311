class Queue():
	def __init__(self):
		self.list = []

	def enqueue(self, x):
		self.list.append(x)

	def dequeue(self):
		assert len(self.list) > 0
		temp = self.list[0]
		del self.list[0]
		return temp

	def peek(self):
		assert len(self.list) > 0
		return self.list[0]

	def size(self):
		return len(self.list)

