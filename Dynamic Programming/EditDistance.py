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

# Simliar to this we are given 2 strings we have to convert one string to other using
 # Minimum number of deletions and insertions 

def minOperations(s1, s2):
    m=len(s1)
    n=len(s2)
    dp=[[0 for i in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif s1[j-1]==s2[i-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    lcs=dp[-1][-1]
    # number of insertions will be len(s1)-length of lcs
    insertions=len(s1)-lcs
    # number of deletions will be len(s2)-length of lcs
    deletions=len(s2)-lcs
    return insertions+deletions