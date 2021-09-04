def kthElement(arr1, arr2, n, m, k):
    # to apply binary search on smaller array
    if (n>m):
        return kthElement(arr2,arr1,m,n,k)
    # because of edge cases 
    low=max(0,k-m)
    high=min(k,n)
    while(low<=high):
        cut1=(low+high)//2
        cut2= k - cut1
        left1 = float('-inf') if cut1==0 else arr1[cut1-1]
        left2 = float('-inf') if cut2==0 else arr2[cut2-1]

        right1 = float('inf') if cut1==n else arr1[cut1]
        right2 = float('inf') if cut2==m else arr2[cut2]
        
        if(left1<=right2 and left2<=right1):
            return max(left1,left2)
        # moving to left
        elif left1>right2:
            high=cut1-1
        # moving to right
        else:
            low=cut1+1
    return -1