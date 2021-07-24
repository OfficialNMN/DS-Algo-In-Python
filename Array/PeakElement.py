# To find any one peak element in an unsorted array
# peak element is an element that is greater than its neighbors

# using Binary Search approach
def peakElement(self,arr, n):
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if ((mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid])):
            return mid
        if (mid>0 and (arr[mid-1]>arr[mid])):
            high=mid-1
        else:
            low=mid+1
    return mid