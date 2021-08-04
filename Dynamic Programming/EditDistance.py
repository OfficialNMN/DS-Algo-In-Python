# Minimum number of operations of create, delete, replace to convert one string to other.

def editDistance(s, t):
	# 2d array to keep track of operations
    dp=[[0 for i in range(len(s)+1)]for j in range(len(t)+1)]
    for i in range(len(s)+1):
        dp[0][i]=i
    for i in range(len(t)+1):
        dp[i][0]=i
    for i in range(1,len(t)+1):
        for j in range(1,len(s)+1):
        	# if letter is equal then copy the prev diagonal element
            if s[j-1]==t[i-1]:
                dp[i][j]=dp[i-1][j-1]
            # else 1+min(adjacent 3 operations)
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return dp[-1][-1]