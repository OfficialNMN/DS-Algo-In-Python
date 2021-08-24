matrix=[[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]]

# A saddle point is a point which is min in its row and max in its column
def saddlepoint(matrix):
	# searching for smallest in row
	for i in range(len(matrix)):
		# consdiering matrix[0][0] as smallest
		svj=0
		for j in range(1,len(matrix[0])):
			# if any other value in row is smaller change the smallest of row
			if matrix[i][j]<matrix[i][svj]:
				svj=j

		# checking if the smallest in columns is also the largest in column
		flag=True
		for k in range(len(matrix)):
			# if the smallest row element is not the largest in its column
			if matrix[k][svj]>matrix[i][svj]:
				flag=False
				break
		if flag==True:
			print(matrix[i][svj])
			return
	# if no such point exists
	print(-1)

saddlepoint(matrix)
