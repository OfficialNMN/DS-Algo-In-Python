def merge_intervals(arr):
	# to sort arr on basis of 1st index
	arr.sort(key = lambda x :x[0])
	result=[arr[0]]
	for i in arr[1:]:
		# if 1st index of i <= 2nd index of last element in result 
		if i[0] <= result[-1][1]:
			# set 2nd index as maximum of 2nd index of i or of last element in result
			result[-1][1] = max(i[1],result[-1][1])
		# simply append i to result as it does not overlap
		else:
			result.append(i)
	return result 

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))