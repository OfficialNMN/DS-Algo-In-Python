def sliding_window(arr,k):
	n=len(arr)
	if n<k:
		return 'Invalid'
	else:
		window_sum=sum(arr[:k])
		max_sum=window_sum
		for i in range(n-k):
			window_sum=window_sum-arr[i]+arr[i+k]
			max_sum=max(window_sum,max_sum)
		return max_sum

print(sliding_window([1,2,3,4,5],3))
