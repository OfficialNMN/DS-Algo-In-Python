# 2. Transpose of a matrix
r=int(input())
c=int(input())
values=[]

for i in range(r):
	values.append(list(map(int,input().split())))

matrix=np.matrix(values)
 
print(matrix.T)
