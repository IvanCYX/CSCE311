from Stack import Stack
from sys import argv

class PostfixEvaluator():
	def __init__(self):
		self.stack = Stack()

	def evaluateExpression(self, expression):
		l = expression.split(' ')
		#iterate over input 
		for x in l:
			#checking for operator
			if isOperator(x):
				#if current element is an operator then pop the top two elements from the stack
				a = self.stack.pop()
				b = self.stack.pop()

				#evalutate the result and push to top of stack
				if x  == '+':
					self.stack.push(b + a)
				elif x == '-':
					self.stack.push(b - a)
				elif x == '*':
					self.stack.push(b * a)
				elif x == '/':
					self.stack.push(b // a)

			else:
				self.stack.push(int(x))

		if self.stack.size() == 1:
			return self.stack.pop()
		elif self.stack.size() > 1:
			return 'Something went wrong... there are still %d elements on the stack' % (self.stack.size())
		else:
			return 'Something went wrong... the stack is empty... :('


def isOperator(self):
	operators = ['+', '-', '/', '*']
	if self in operators:
		return True
	else:
		return False

if __name__ == '__main__':
	p = PostfixEvaluator()
	print (p.evaluateExpression(argv[1]))