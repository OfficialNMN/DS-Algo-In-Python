'''Arod of length N inches and an array of prices, price[] that contains prices of 
all pieces of size smaller than N. Determine the maximum value obtainable by jting up 
the rod and selling the pieces'''

# Exactly similar to Unbounded Knapsack problem with below analogy
'''
W - length of array
n - N
profit - price
wt - length array'''

def cutRod(price, n):
	# creating an array of every cut possible
	length=[i for i in range(1,n+1)]
	dp=[[0 for i in range(n+1)] for i in range(n+1)]
	for i in range(n+1):
		for j in range(n+1):
			# if either length of rod is 0 or price is 0
			if i==0 or j==0:
				dp[i][j]=0
			# if length is less than maxlength at that stage
			# then consider if it maximises profit else discard
			elif length[i-1] <= j:          
				dp[i][j]=max(price[i-1]+dp[i][j-length[i-1]],dp[i-1][j])
			# if length is greater than maxlength
			else:
				dp[i][j]=dp[i-1][j]       
	return dp[-1][-1]

print(cutRod([1, 5, 8, 9, 10, 17, 17, 20],8))