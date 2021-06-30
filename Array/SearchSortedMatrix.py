import numpy as np

matrix=[[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]]


def search(ele):
	# initial i(move down),j(move left) is at the last element of first row
	i=0
	j=len(matrix[0])-1
	# traverse till i<len(matrix) and j>0
	while(i<len(matrix) and j>=0):
		if ele==matrix[i][j]:
			print(i,end=",")
			print(j)
			return  
		# if ele is smaller then move to left
		elif ele<matrix[i][j]:
			j-=1
		# else move down
		else:
			i+=1
	print(-1)

search(43) 

