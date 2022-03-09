def bubbleSort(seq):
	n = len(seq)
	#perform n-1 bubble operations on the sequence
	for i in range (n - 1):
		#bubble the largest item to the end
		for j in range (n - i - 1):
			#swapping jth and j+1th items
			if seq[j] > seq[j + 1]:
				temp = seq[j]
				seq[j] = seq[j + 1]
				seq[j + 1] = temp


def selectionSort(seq):
	n = len(seq)
	for i in range (n - 1):
		#assume ith element to be the smallest
		smallIndex = i
		for j in range (i + 1, n):
			#find a smaller value
			if seq[j] < seq[smallIndex]:
				smallIndex = j
				#swap the ith value and new smallest value only if
				#its not alreaey in its proper position
		if smallIndex != i:
			temp = seq[i]
			seq[i] = seq[smallIndex]
			seq[smallIndex] = temp


def insertionSort(seq):
	n = len(seq)
	#starts with the first item as the only sorted entry
	for i in range (n - 1):
		#value to be indexed
		value = seq[i]
		#position where alue fits in the ordered list
		pos = i
		while pos > 0 and value < seq[pos - 1]:
			#shift items to the right during search
			seq[pos] = seq[pos - 1]
			pos -= 1
		#put saved value into the open space
		seq[pos] = value
   
