# To find longest increasing subsequence in the given array
# Time complexity - O(n^2)

def longestSubsequence(a,n):
    dp=[1]*n
    for i in range(1,n):
        # to check smaller elements than current in given array
        for j in range(0,i):
            if a[i]>a[j] and dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
    return max(dp)

print(longestSubsequence([10,22,9,33,21,50,41,60],8))

# Optimized approach using binary search
# Time complexity - O(nlogn)

def longestSubsequence(a,n):
    tail=[]
    tail.append(a[0])
    for i in range(1,n):
        if a[i]>tail[-1]:
            tail.append(a[i])
        else:
            c=ceil_idx(tail,0,len(tail)-1,a[i])
            tail[c]=a[i]
    return len(tail)

def ceil_idx(tail,low,high,x):
    while(low<high):
        mid=(low+high)//2
        if tail[mid]>=x:
            high=mid
        else:
            low=mid+1
    return high

# Maximum sum increasing subsequence

def maxSumIS(Arr, n):
    dp=[0]*n
    for i in range(len(dp)):
        maxi=None
        for j in range(i):
            if Arr[j]<Arr[i]:
                # to handle first element 
                if maxi==None:
                    maxi=dp[j]
                # to handle case when dp[j]>maxi
                elif dp[j]>maxi:
                    maxi=dp[j]
        # to handle case when element is smallest of previous
        if maxi==None:
            dp[i]=Arr[i]
        else:
            dp[i]=maxi+Arr[i]
    return max(dp)