# Maximum number of ways for making the given sum using given array of coins
'''
S-> array of coins
n-> sum to be made using coins
m-> number of coins given
'''

def countways(S, m, n): 
	dp=[[0 for i in range(n+1)] for i in range(m+1)]
	# base inititalisation
	for i in range(n+1):
	    dp[0][i]=0
	for i in range(m+1):
	    dp[i][0]=1
	for i in range(1,m+1):
		for c in range(1,n+1):
			# if current coin value is less than sum to be made
			if S[i-1] <= c:          
				# either take the coin or reject it  
				dp[i][c]= dp[i][c-S[i-1]] + dp[i-1][c]
			else:
				# coin will not be taken therefore previous row value is taken
				dp[i][c]=dp[i-1][c]       
	return dp[-1][-1]

print(countways([1,2,3],3,4))

# Minimum number of coins for making the sum
