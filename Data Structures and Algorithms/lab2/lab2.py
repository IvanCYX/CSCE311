#from matK import *
from matKomplete import *

def main():
	entries=[None,None,None]
	with open('matrices.txt') as f:
		i=0
		for line in f:
			entries[i] = line.strip().split(',')
			i+=1
	
	leftHandMatrix = Matrix(3,3)
	k=0
	for i in range(0,3):
		for j in range(0,3):
			leftHandMatrix.set((i,j),int(float(entries[0][k])))
			k+=1

	rightHandMatrix = Matrix(3,3)
	k=0
	for i in range(0,3):
		for j in range(0,3):
			rightHandMatrix.set((i,j),int(float(entries[1][k])))
			k+=1
	print ('Left Matrix :\n', leftHandMatrix,'\n')
	print ('Right Matrix:\n', rightHandMatrix,'\n')
	print ('Add         :\n',leftHandMatrix.add(rightHandMatrix),'\n')
	print ('Subtract    :\n',leftHandMatrix.sub(rightHandMatrix),'\n')
	print ('Multiply    :\n',leftHandMatrix.multiply(rightHandMatrix),'\n')
	print ('Transpose   :\n',leftHandMatrix.transpose(),'\n')
	print ('Trace       :\n',leftHandMatrix.trace())

if __name__ == '__main__':
	main()
