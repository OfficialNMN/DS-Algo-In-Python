# TimeComplexity----O(n)

def LinearSearch(arr,n,num):
    for i in range(n):
        if (num==arr[i]):
            return i
    return -1

print(LinearSearch([1,2,3,4,5],5,3))