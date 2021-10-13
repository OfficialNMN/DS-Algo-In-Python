# To get number of unique paths from starting of matrix to end of matrix

# Recursive solution is very time and space inefficient
def uniquePaths(m,n):
    # creating a 2d dp to store paths
    dp=[[0 for _ in range(n)] for _ in range(m)]
    
    # initialising 1st row and 1st column as 1
    for i in range(n):
        dp[0][i]=1
    for i in range(m):
        dp[i][0]=1
    
    # path for dp[i][j] is sum of previous row and column value
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    # answer will be the value in last cell of dp
    return dp[-1][-1]