'''Trapping Rain Water'''

# TimeComplexity----O(n)
# SpaceComplexity---O(1)

def trappingWater( arr,n):
    lmax=[0 for i in range(n)]
    rmax=[0 for i in range(n)]
    water=0
    # leftmax array
    lmax[0]+=arr[0]
    for i in range(1,n):
        lmax[i]+=max(arr[i],lmax[i-1])
    # rightmax array
    rmax[-1]+=arr[n-1]
    for i in range(n-2,-1,-1):
        rmax[i]+=max(arr[i],rmax[i+1])
    for i in range(n):
        # water stored is min(left,right)-a[i]
        water+=min(lmax[i],rmax[i])-arr[i]
    return water

print(trappingWater([3, 0, 2, 0, 4],5))
