# 3. Searching in a row and column wise sorted matrix
def search(matrix,n,x):
	i=0
	j=n-1
	while(i<n and j>=0):
		if matrix[i][j]==x:
			return i,j
		elif matrix[i][j]>x:
			j-=1
		else:
			i+=1
	return -1

mat=[[10, 20, 30, 40], 
      [15, 25, 35, 45], 
      [27, 29, 37, 48], 
      [32, 33, 39, 50]]

print(search(mat,4,29))
