# Longest palindromic subsequence

'''We are given a string and we have to find lps, For Eg: lps of ELERMENMET----->EMEME
This can be done by calling lcs on given string and reverse of given string
and the result of lcs will be the length of lps in the given string
'''

def longestPalindromeSubseq(s):
	# reversing given string
    s1=s[::-1]
    # calling lcs on s and reverse of s
    return lcs(s,s1)

def lcs(s,s1):
    x=len(s)
    y=len(s1)
    dp=[[0 for i in range(y+1)] for j in range(x+1)]
    for i in range(x+1):
        for j in range(y+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif s[i-1]==s1[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]


print(longestPalindromeSubseq('ELERMENMET'))


''' We are given a string and have to calculate minimum number of deletions to make the 
a subsequence from the given string palindrome.

number of deletions is inversely proportional to length of lps
therefore, minimum deletions = length of string - lps 
'''