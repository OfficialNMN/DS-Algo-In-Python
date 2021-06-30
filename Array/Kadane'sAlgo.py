def maxSubArraySum(a,size):
	local_sum=0
	max_sum=0
	for i in range(size):
		local_sum=max(a[i],a[i]+local_sum)
		if local_sum>max_sum:
			max_sum=local_sum
	return max_sum

print(maxSubArraySum([1,2,3,-2,5],5))