# arr is the position of stalls
# n is the number of cows
def AggresiveCows(arr,n):
    low=1
    high=a[-1]-a[0]
    result=-1
    while(low<=high):
        mid=(low+high)//2
        # if cows can be placed in calculated mid
        # we try to maximise it
        if canplace(arr,n,mid):
            result=mid
            low=mid+1
        else:
            high=mid-1
    return result

def canplace(arr,n,dist):
    # position of first cow 
    pos=arr[0]
    # count of number of cows
    count=1
    for i in range(len(arr)):
        # if condition is satisfied then count is increased
        if arr[i]-pos>=dist:
            count+=1
            pos=a[i]
        if count==n:
            return True
    return False