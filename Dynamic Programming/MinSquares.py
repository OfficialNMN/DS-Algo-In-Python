import sys 
import numpy as np

def minsquares(n,dp):
	if n==0:
		return 0
	ans=sys.maxsize
	root=int(np.sqrt(n))
	for i in range(1,root+1):
		if n-(i**2) not in dp:
			dp[n-(i**2)]=minsquares(n-(i**2),dp)
			currans=1+dp[n-(i**2)]
		currans=1+dp[n-(i**2)]
	return min(ans,currans)

dp={}
print(minsquares(41,dp))