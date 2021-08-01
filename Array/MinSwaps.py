# Minimum number of swaps required to sort the array

def minSwaps(nums):
    arr=[(i,nums.index(i)) for i in nums]
    arr.sort()
    print(arr)
    count=0
    i=0
    while (i<len(arr)):
        if arr[i][1]==i:
            i+=1
        else:
            temp=arr[i][1]
            count+=1
            arr[i],arr[temp]=arr[temp],arr[i]
    return count
print(minSwaps([13, 1, 5, 3, 6, 11, 10]))