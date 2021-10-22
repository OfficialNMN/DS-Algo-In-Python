# To calculate Longest Common Substring in the given 2 strings 

def lcsubstring(s1,s2,x,y):
    dp=[[0 for i in range(y+1)] for j in range(x+1)]
    for i in range(x+1):
        for j in range(y+1):
        	# when length of either of 2 strings is 0 then no lcs possible
            if i==0 or j==0:
                dp[i][j]=0
            # if character matches increase previous diagonal value
            elif s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            # if not matches then 0 as the length of common substring is reset to 0
            else:
                dp[i][j]=0
    # answer will be the maximum value in the matrix
    maxi=float('-inf')
    for i in range(x+1):
        for j in range(y+1):
            if dp[i][j]>maxi:
                maxi=dp[i][j]
    return maxi

print(lcsubstring('ABCDGH','ACDGHR',6,6))