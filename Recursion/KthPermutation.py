def getPermutation(n,k):
    nums=[str(i) for i in range(1,n+1)]
    result=[]
    # beacause of 0 based indexing
    fact=math.factorial(n)
    index=k-1
    while nums:
        # when first number gets fixed permutaions to arrange next numbers
        fact=fact//len(nums)
        # position of the number in list
        pos=index//fact
        number=nums.pop(pos)
        result.append(number)
        # index for next number as problem keeps decreasing  
        index=index%fact
    return "".join(result)