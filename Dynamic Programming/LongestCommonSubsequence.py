''' To calculate the length of longest common subsequence present in 2 given strings '''

def lcs(x,y):
	m=len(x)
	n=len(y)

	# creating an empty matrix of size (n+1 X m+1) to store values
	L=[[None]*(n+1) for i in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				L[i][j]=0
			elif x[i-1] == y[j-1]:                   # if the letter matches in 2 strings then increment the previous diagonal value
				L[i][j] = L[i-1][j-1]+1       
			else:
				L[i][j] = max(L[i-1][j],L[i][j-1])   # if not matched then find the max of value of previous row or previous column
	return L[m][n]

print(lcs('ABCD','BDAA'))
