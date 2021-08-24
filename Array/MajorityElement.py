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

#   The majority element II is that appears more than ⌊n / 3⌋ times
def majorityElement(nums):
    # Boyer Moore Algo as in this at max 2 majority elements would be there
    num1=-1
    num2=-1
    count1=0
    count2=0
    for i in nums:
        if i==num1:
            count1+=1
        elif i==num2:
            count2+=1
        elif count1==0: 
            num1=i
            count1+=1
        elif count2==0:
            num2=i
            count2+=1
        else:
            count1-=1
            count2-=1
    ans=[]
    # checking if count of num1 and num2 is greater than ⌊n / 3⌋ times
    if nums.count(num1)>math.floor(len(nums)/3):
        ans.append(num1)
    if nums.count(num2)>math.floor(len(nums)/3):
        ans.append(num2)
    return ans