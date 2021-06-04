def maxGold(n, m, M):
    dp=[[0 for i in range(m)] for j in range(n)]
    for j in range(m-1,-1,-1):
        for i in range(n):
            if j==m-1:
                dp[i][j]=M[i][j]
            elif i==0:
                dp[i][j]=M[i][j]+max(dp[i][j+1],dp[i+1][j+1])
            elif i==n-1:
                dp[i][j]=M[i][j]+max(dp[i][j+1],dp[i-1][j+1])
            else:
                dp[i][j]=M[i][j]+max(dp[i-1][j+1],dp[i][j+1],dp[i+1][j+1])
    maxi=dp[0][0]
    for i in range(1,len(dp)):
        if dp[i][0]>maxi:
            maxi=dp[i][0]
    return maxi

print(maxGold(4,4,[[1,3,1,5],[2,2,4,1],[5,0,2,3],[0,6,1,2]]))