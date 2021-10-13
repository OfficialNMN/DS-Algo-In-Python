def nCr(n, k):
    dp=[[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(n+1):
        # taking min because when k>n dp[i][j] will be 0
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                dp[i][j]=1
            else:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
    return dp[n][k]%1000000007

print(nCr(3,2))