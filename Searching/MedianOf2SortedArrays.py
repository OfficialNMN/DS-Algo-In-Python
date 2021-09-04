
def findMedianSortedArrays(nums1, nums2):
    # To do binary seach on the smaller nums
    if len(nums2)<len(nums1):
        return findMedianSortedArrays(nums2, nums1)
    n1=len(nums1)
    n2=len(nums2)
    low=0
    high=n1
    while(low<=high):
        # cut1 is in nums1
        cut1=(low+high)//2
        # cut2 is in nums2
        cut2=(n1+n2+1)//2 - cut1
        
        left1 = float('-inf') if cut1==0 else nums1[cut1-1]
        left2 = float('-inf') if cut2==0 else nums2[cut2-1]

        right1 = float('inf') if cut1==n1 else nums1[cut1]
        right2 = float('inf') if cut2==n2 else nums2[cut2]
        
        if(left1<=right2 and left2<=right1):
            # if combined length is even
            if (n1+n2)%2==0:
                return (max(left1,left2)+min(right1,right2))/2
            # if length is odd
            else:
                return max(left1,left2)
        elif left1>right2:
            high = cut1-1
        else:
            low = cut1+1
    # in this case arrays are not sorted
    return 0.0            