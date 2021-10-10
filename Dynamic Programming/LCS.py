# Longest Common Subsequence using divide and conquer

def lcs(s1,s2,index1,index2):
	if index1==len(s1) or index2==len(s2):
		return 0
	if s1[index1]==s2[index2]:
		return 1+lcs(s1,s2,index1+1,index2+1)
	else:
		option1=lcs(s1,s2,index1,index2+1)
		option2=lcs(s1,s2,index1+1,index2)
		return max(option1,option2)

print(lcs('abcde','ade',0,0))

# using DP where x any are respective lengths of s1 and s2
def lcs(x,y,s1,s2):
    dp=[[0 for i in range(y+1)] for j in range(x+1)]
    for i in range(x+1):
        for j in range(y+1):
        	# dp[i][j] will be 0 when _ character is there
            if i==0 or j==0:
                dp[i][j]=0
            # if character matches increase previous diagonal value
            elif s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            # if not matches then take max of prev row and prev col value
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]
