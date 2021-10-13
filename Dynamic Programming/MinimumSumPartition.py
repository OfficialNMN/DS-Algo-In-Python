# To do partition of array in a way such that the difference of the sum of those 2 
# subarrays is minimum

def minDifference(arr, n):
	# applying SubsetSum to arr with sum(arr) as target
	# to get what all sums are possible
    s=sum(arr)
	dp=[[0 for _ in range(s+1)] for i in range(n+1)]
	
	for i in range(s+1):
	    dp[0][i]=0
	for i in range(n+1):
	    dp[i][0]=1
	   
	for i in range(1,n+1):
	    for j in range(1,s+1):
	        if arr[i-1]<=j:
	            dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
	        else:
	            dp[i][j]=dp[i-1][j]
	# minimise s1 - s2 = diff
	# sum = s1 + s2 --> s2 = sum - s1 --> diff = sum - 2*s1
	# find the maximum traversing back from middle of last row of dp 
	# for which SubsetSum which is true
	for i in range(s//2,-1,-1):
	    if dp[n][i]==True:
	        diff=s-(2*i)
	        break
	return diff