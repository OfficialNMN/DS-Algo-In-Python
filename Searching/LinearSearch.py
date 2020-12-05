# TimeComplexity----O(n)

def LinearSearch(arr,n,num):
    for i in range(n):
        if (num==arr[i]):
            return i
    return -1
