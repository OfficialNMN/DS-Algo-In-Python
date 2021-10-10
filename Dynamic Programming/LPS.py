# Longest palindromic subsequence
# For Eg lps of ELERMENMET----->EMEME

def lps(s,start,end):
	if start > end:
		return 0 
	elif start==end:
		return 1
	elif s[start]==s[end]:
		return 2+lps(s,start+1,end-1)
	else:
		option1=lps(s,start,end-1)
		option2=lps(s,start+1,end)
		return max(option1,option2)

print(lps('ELERMENMET',0,8))
