# We can do xor of all elements and element that occurs once will be the result
# after xor ---> O(n) solution.

# O(logn) solution usingn Binary Search

# In left half we observe-
# 1st instance - even index
# 2nd instance - odd index

# In right half we observe-
# 1st instance - odd index
# 2nd instance - even index

def findOnce(arr, n):
    low=0
    # keeping high at second last so as if target is the last element
    high=n-2
    while(low<=high):
        mid=(low+high)//2
        # if (mid^1) is odd we get prev even
        # while if (mid^1) is even we get next odd
        if (arr[mid]==arr[mid^1]):
            low=mid+1
        else:
            high=mid-1
    # low index will have the answer
    return arr[low]