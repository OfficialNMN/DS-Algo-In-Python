''' 0/1 Knapsack Problem 
W - capacity of bag
profit - profit of each item
wt -  weight of each item
n - number of total items '''

# Time Complexity: O(n*W) using BottomUp Approach without memoization

def sack(W,wt,profit,n):
	# building empty nXW matrix to fill profit values as wt increases
	k=[[0 for i in range(W+1)] for i in range(n+1)]
	for i in range(n+1):
		for w in range(W+1):
			if i==0 or w==0:
				k[i][w]=0
			elif wt[i-1] <= w:          # means that if bag capacity is greater than wieght of current item
				k[i][w]=max(profit[i-1]+k[i-1][w-wt[i-1]],k[i-1][w])
			else:
				k[i][w]=k[i-1][w]       # if not then fill in the previous value
	return k[n][w]


print(sack(50,[10,20,30],[60,100,120],3))	
			
