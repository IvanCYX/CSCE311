from Queue import Queue
from Stack import Stack


class More():
	def __init__(self, book):
		self.q = Queue()
		#open the book
		b = open(book)
		#read lines
		b = b.readlines()
		#put each line into the queue
		for i in b:
			self.q.enqueue(i)

	def display(self, lines):
		while lines > 0:
			s = Stack()
			#remove top element from the queue and put into top of stack
			s.push(self.q.dequeue())
			#print top element of stack
			print(s.pop())
			#go down the lines until none remain
			lines -= 1


if __name__ == '__main__':
	m = More('text2.txt')
	m.display(20)