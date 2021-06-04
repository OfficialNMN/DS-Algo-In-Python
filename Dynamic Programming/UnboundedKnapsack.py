''' This is similar to knapsack but here we can take any number of weights in the 
bag to maximise the profit.
Since in this case we will have duplicate weights so we will use a 1D array '''

def unboundKnap(weights,values,capacity):
	dp=[0 for _ in range(capacity+1)]
	# because when cap is 0 profit will be 0
	for cap in range(1,capacity+1):
		maxi=0
		for i in range(len(weights)):
			if weights[i]<=cap:
				# remaining bag capacity
				rbagc=cap-weights[i]
				# remaining bag value
				rbagv=dp[rbagc]
				# total bag value for current chosen item
				tbagv=rbagv+values[i]

				if tbagv>maxi:	
					maxi=tbagv	
		dp[cap]=maxi
	return dp[-1]

print(unboundKnap([2,5,1,3,4],[15,14,10,45,30],7))		
