from copy import deepcopy as copy
class Matrix:
	def __init__(self,row,col):
		self.matrix = []
		self.row    = row
		self.col    = col
		for i in range(0,row):
			tempList = []
			for j in range(0,col):
				tempList.append(0)
			self.matrix.append(tempList)

	#Sets the value at a certain entry
	def set(self,entry,value):
		assert entry[0]<self.row and entry[1]<self.col
		self.matrix[entry[0]][entry[1]]=value
	
	#Gets the value at a certain entry
	def get(self,entry):
		return self.matrix[entry[0]][entry[1]]

	#Scales each entry by a value
	def scale(self,scalar):
		tMatrix = copy(self)
		for i in range(0,self.row):
			for j in range(0,self.col):
				tMatrix.set((i,j),self.matrix[i][j]*scalar)
		return tMatrix

	#Matrix addition
	def add(self,rhm):
		tmatrix = copy(self)
		assert tmatrix.row == rhm.row and tmatrix.col == rhm.col
		temp = Matrix(tmatrix.row,tmatrix.col)
		for i in range(0, tmatrix.row):
			for j in range(0, tmatrix.col):
				tValue = tmatrix.get((i,j))+rhm.get((i,j))
				temp.set( (i,j) , tValue)
		return temp
				
	#Matrix subtraction
	def sub(self,rhm):
		tmatrix = copy(self)
		assert tmatrix.row == rhm.row and tmatrix.col == rhm.col
		temp = Matrix(tmatrix.row,tmatrix.col)
		for i in range(0, tmatrix.row):
			for j in range(0, tmatrix.col):
				tValue = tmatrix.get((i,j))-rhm.get((i,j))
				temp.set( (i,j) , tValue)
		return temp

	#Matrix multiplication
	def multiply(self,rhm):
		tmatrix = copy(self)
		assert tmatrix.row == rhm.row and tmatrix.col == rhm.col
		temp = Matrix(tmatrix.row,tmatrix.col)
		for i in range(0, tmatrix.row):
			for j in range(0, rhm.col):
				tValue = 0
				for k in range(0, rhm.col):
					tValue += (tmatrix.get((i, k)) * rhm.get((k, j)))
					temp.set((i, j), tValue)
		return temp
				
				
	#Matrix Transposition
	def transpose(self):
		tmatrix = copy(self)
		temp = Matrix(tmatrix.row, tmatrix.col)
		for i in range(0, tmatrix.row):
			for j in range(0, tmatrix.col):
				temp.set((j, i), tmatrix.get((i, j)))
		return temp

	#Sum of the diagonals in a square matrix
	def trace(self):
		tmatrix = copy(self)
		principal = 0
		for i in range(0, tmatrix.row):
			for j in range(0, tmatrix.col):
				if i == j:
					principal += tmatrix.get((i, j))

		return principal



	def __str__(self):
		string ="" 
		for i in range(0, self.row):
			for j in range(0,self.col):
				string += '%4s'%(str(self.matrix[i][j])) + " " 
			string += "\n"
		string = string[:-2]
		return string
