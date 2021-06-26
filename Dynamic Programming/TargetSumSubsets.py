# To check whether there exists a subset in arr which can sum upto gievn target
n=5
arr=[4,2,3,1,7]
target=10

# creating a dp 0f (n+1)x(target+1)
dp=[[False for i in range(target+1)] for j in range(n+1)]
for i in range(len(dp)):
	for j in range(len(dp[0])):
		# first cell is always True
		if i==0 and j==0:
			dp[i][j]=True
		# first row is False for every column except first
		elif i==0:
			dp[i][j]=False
		# first col is always true
		elif j==0:
			dp[i][j]=True
		else:
			# if previous num can make target
			if dp[i-1][j]==True:
				dp[i][j]=True
			else:
				# assigning value of current arr element
				val=arr[i-1]
				# only proceed when current target > val
				if j>=val:
					# if previous arr elements except current true or not
					if dp[i-1][j-val]==True:
						dp[i][j]=True

print(dp[n][target])