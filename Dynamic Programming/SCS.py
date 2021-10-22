# To find Shortest Common Supersequence of given two strings

''' SCS means a squence that contains both the strings and is of shortest possible length
length of SCS = (m+n) - length of LCS

this is because for supersequence of worst case(where both strings can be joined together)
to be shortest in length we can remove one lcs from the supersequence
'''

def shortestCommonSupersequence(s1, s2, x, y):
    dp=[[0 for i in range(y+1)] for j in range(x+1)]
    for i in range(x+1):
        for j in range(y+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    # SCS = (sum of length of 2 strings)-(length of LCS)
    return (x+y)-dp[-1][-1]

# Print SCS
def print_scs(s1,s2,m,n):
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
    # in case of scs we will traverse till i>0 or j>0
    # this means even if one string has been exhausted other will still traverse
    while(i>0 or j>0):
        # append to answer when element is same
        if s1[i-1]==s2[j-1]:
            ans.append(s1[i-1])
            i-=1
            j-=1
        else:
            # if element is not same still append in scs
            if t[i-1][j]>t[i][j-1]:
                ans.append(s1[i-1])
                i-=1
            else:
                ans.append(s2[j-1])
                j-=1
    # reverse the answer 
    ans.reverse()
    return ''.join(ans)

print(print_scs('ABCD','BDAA',4,4))