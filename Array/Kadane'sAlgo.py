def maxSubArraySum(nums):
	# initializing local_sum = 0 and max_sum to nums[0]  
    local_sum=0
    max_sum=nums[0]
    # iterate through the array and add nums[i] to local_sum
    for i in range(len(nums)):
        local_sum+=nums[i]
        # if local > max then change max_sum to local_sum
        if local_sum>max_sum:
            max_sum=local_sum
        # if local_sum < 0 we reset it to 0
        if local_sum < 0:
            local_sum=0
    return max_sum

print(maxSubArraySum([1,2,3,-2,5]))