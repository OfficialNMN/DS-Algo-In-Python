def longestPalin( s):
    # result string
    res=''
    for i in range(len(s)):
        # for odd length
        temp=self.helper(i,i,s)
        if len(res)<len(temp):
            # if length increases
            res=temp
        # for even length
        temp=self.helper(i,i+1,s)
        if len(res)<len(temp):
            res=temp
    return res

def helper(l,r,s):
    # if inbound and is palindrome
    while(l>=0 and r<len(s) and s[l]==s[r]):
        l-=1
        r+=1
    return s[l+1:r]
        