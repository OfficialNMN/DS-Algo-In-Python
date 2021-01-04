# 1. To take matrix input and print matrix in snake form
r=int(input())
c=int(input())
values=list(map(int,input().split()))

matrix=np.array(values).reshape(r,c)

def snake_print(matrix):
	for i in range(r):
		if i%2==0:
			for j in range(c):
				print(str(matrix[i][j]),end=' ')
		else:
			for j in range(c-1,-1,-1):
				print(str(matrix[i][j]),end=' ')

snake_print(matrix)
