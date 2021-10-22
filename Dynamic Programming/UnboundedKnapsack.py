''' Unbounded Knapsack Problem 
W - capacity of bag
n - number of total items
profit - profit of each item
wt -  weight of each item'''

# Time Complexity: O(n*W)

''' This is similar to knapsack but here we can take unlimited number of items in the 
bag to maximise the profit. '''

def unboundKnap(W,wt,profit,n):
	# building empty (n+1 X W+1) i.e (items X weight) matrix to fill profit values as wt increases
	dp=[[0 for i in range(W+1)] for i in range(n+1)]
	for i in range(n+1):
		for w in range(W+1):
			if i==0 or w==0:
				dp[i][w]=0
			# replacing i by (i-1) since unlimited items are present
			elif wt[i-1] <= w:          
				dp[i][w]=max(profit[i-1]+dp[i][w-wt[i-1]],dp[i-1][w])
			else:
				dp[i][w]=dp[i-1][w]       
	return dp[-1][-1]

print(unboundKnap(8,[1,3,4,5],[1,4,5,7],4))		
