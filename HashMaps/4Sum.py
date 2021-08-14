def fourSum(nums, target):
    nums.sort()
    ans=[]
    # fixing two pointers i,j
    for i in range(len(nums)-3):
        # checking for duplicates for i pointer
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,len(nums)-2):
            # checking for duplicates for j pointer
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            # making 2 pointers left and right for the remaining subarray
            left=j+1
            right=len(nums)-1
            while(left<right):
                # if unique quadruple is found
                if (nums[i]+nums[j]+nums[left]+nums[right]==target):
                    ans.append([nums[i],nums[j],nums[left],nums[right]])
                    left+=1
                    right-=1
                    # checking for duplicates for left pointer
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    # # checking for duplicates for right pointer
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif (nums[i]+nums[j]+nums[left]+nums[right]<target):
                    left+=1
                else:
                    right-=1
    return ans 