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