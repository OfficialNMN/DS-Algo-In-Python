def nextPermutation(nums):
    # index1 is to store index of element that is greater than its previous 
    index1=0
    for i in range(len(nums)-1,0,-1):
        if nums[i-1]<nums[i]:
            index1=i
            break
    # if index1 is not found simply reverse array as its the last permutation
    if index1==0:
        nums.reverse()
        return
    # index2 is to store the next greater element of index1
    index2=len(nums)-1
    while (nums[index1-1]>=nums[index2]):
        index2-=1
    # swapping of index1 element with index2
    nums[index1-1],nums[index2]=nums[index2],nums[index1-1]
    # reversing the array index1 onwards to get the next smallest permutation 
    nums[index1:]=nums[index1:][::-1]