# To check whether there exists a subset in arr which can sum upto given target

# This problem is an similar to knapsack problem 

def isSubsetSum (N, arr, sum):
    dp=[[0 for i in range(sum+1)] for _ in range(N+1)]
    # complete first row is 0 bcoz sum cannot be more than 0 when subset is empty
    for i in range(sum+1):
        dp[0][i]=0
    # complete first col is 1 bcoz empty subset gives sum=0
    for i in range(N+1):
        dp[i][0]=1
    for i in range(1,N+1):
        for j in range(1,sum+1):
            # case when arr element will be included 
            if arr[i-1]<=j:
                # in case of counting how many subsets have the sum replace or by +
                dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
            # when element will be skipped
            elif arr[i-1]>j:
                dp[i][j]=dp[i-1][j]
    return dp[N][sum]        
