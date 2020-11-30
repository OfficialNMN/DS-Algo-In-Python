# TimeComplexity----O(log(n))

def BinarySearch(arr,n,num):
    left=0
    right=n-1
    while(left<=right):
        mid=(left+right)//2
        if (num==arr[mid]):
            return mid
        elif (num>arr[mid]):
            left=mid+1
        else:
            right=mid-1
    return -1

print(BinarySearch([1,2,3,4,5],5,4))
        