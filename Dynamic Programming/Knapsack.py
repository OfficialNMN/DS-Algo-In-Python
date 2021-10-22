''' 0/1 Knapsack Problem 
W - capacity of bag
n - number of total items
profit - profit of each item
wt -  weight of each item'''

# Time Complexity: O(n*W) using BottomUp Approach 

def sack(W,wt,profit,n):
	# building empty (n+1 X W+1) i.e (no. of items X capacity) matrix to fill profit values as wt increases
	dp=[[0 for i in range(W+1)] for i in range(n+1)]
	for i in range(n+1):
		for w in range(W+1):
			if i==0 or w==0:
				dp[i][w]=0
			# if bag capacity reamining is greater than wieght of current item
			elif wt[i-1] <= w:          
				dp[i][w]=max(profit[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
			# if not then fill in the previous value
			else:
				dp[i][w]=dp[i-1][w]       
	return dp[-1][-1]


print(sack(50,[10,20,30],[60,100,120],3))	
			
