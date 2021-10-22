# Longest Common Subsequence
# Given 2 strings with their respective lengths and find lcs

# Recursive + Memoized version
def longestCommonSubsequence(text1, text2):
    m=len(text1)
    n=len(text2)
    # making a store for overlapping subproblems
    t=[[-1 for i in range(n+1)] for i in range(m+1)]
    return lcs(text1,text2,m,n,t)

# helper function
def lcs(text1,text2,m,n,t):
    # either of 2 strings is empty
    if m==0 or n==0:
        return 0
    # check if t[m][n] has some value or not
    if t[m][n]!=-1:
        return t[m][n]
    # traversing from end if elements are equal call 1+lcs() with trimming both strings
    if text1[m-1]==text2[n-1]:
        # store the derived lcs value in the matrix
        t[m][n]=1+lcs(text1,text2,m-1,n-1,t)
        return t[m][n]
    # trim the second string and search lcs or trim the first string and search lcs
    t[m][n] = max(lcs(text1,text2,m-1,n,t),lcs(text1,text2,m,n-1,t))
    return t[m][n]

print(longestCommonSubsequence('abcd','bdaa'))

# using DP approach
def lcs_dp(s1,s2,x,y):
    dp=[[0 for i in range(y+1)] for j in range(x+1)]
    for i in range(x+1):
        for j in range(y+1):
        	# when length of either of 2 strings is 0 then no lcs possible
            if i==0 or j==0:
                dp[i][j]=0
            # if character matches increase previous diagonal value
            elif s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            # if not matches then take max of prev row and prev col value
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    # answer will be stored in the last cell of matrix
    return dp[-1][-1]

print(lcs_dp('ABCD','BDAA',4,4))

# To print that lcs

def print_lcs(s1,s2,m,n):
    t=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            # when length of either of 2 strings is 0 then no lcs possible
            if i==0 or j==0:
                t[i][j]=0
            # if character matches increase previous diagonal value
            elif s1[i-1]==s2[j-1]:
                t[i][j]=1+t[i-1][j-1]
            # if not matches then take max of prev row and prev col value
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    # after creating the lcs dp table start from last cell
    i,j=m,n
    ans=[]
    # traverse till i>0 and j>0 
    while(i>0 and j>0):
        # append to answer when element is same
        if s1[i-1]==s2[j-1]:
            ans.append(s1[i-1])
            i-=1
            j-=1
        else:
            # if element is not same move to max(t[i-1][j],t[i][j-1])
            if t[i-1][j]>t[i][j-1]:
                i-=1
            else:
                j-=1
    # reverse the answer 
    ans.reverse()
    return ''.join(ans)

print(print_lcs('ABCD','BDAA',4,4))