#   The majority element is that appears more than ⌊n / 2⌋ times.
def majorityElement(nums):
    # Moore's voting Algo
    num=0
    count=0
    for i in nums:
        # if count is 0 make num=i
        if count==0:
            num=i
        # check if i==num then count+=1
        if i==num:
            count+=1
        else:
            count-=1
    return num