import sys

# Reduce number to 1 in minimum steps

def minSteps(n,dp):
	ans1=sys.maxsize
	if n==1:
		return 0
	if n%3==0:
		if n not in dp:
			ans1=minSteps(n//3,dp)
			dp[n//3]=ans1
		ans1=dp[n//3]
	ans2=sys.maxsize
	if n%2==0:
		if n not in dp:
			ans2=minSteps(n//2,dp)
			dp[n//2]=ans2
		ans2=dp[n//2]
	ans3=sys.maxsize
	if n not in dp:
		ans3=minSteps(n-1,dp)
		dp[n-1]=ans3
	ans3=dp[n-1]
	return 1+min(ans1,ans2,ans3)

dp={}
print(minSteps(9,dp))