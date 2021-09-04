# searching using binary search
def search(A ,key ):
    low=0
    high=len(A)-1
    while(low<=high):
        mid=(low+high)//2
        if A[mid]==key:
            return mid
        # to check if left half is sorted
        elif A[low]<=A[mid]:
            if (key>=A[low] and key<=A[mid]):
                high=mid-1
            else:
                low=mid+1
        # checking if right half is sorted
        else:
            if (key>=A[mid] and key<=A[high]):
                low=mid+1
            else:
                high=mid-1
    return -1