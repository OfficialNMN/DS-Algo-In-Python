from collections import deque

def max_of_subarrays(arr,n,k):
    result=[0 for i in range(n-k+1)]
    ind=0
    q=deque()
    for i in range(n):
        # remove elements from front which are out of window size
        if (len(q)!=0 and q[0]==i-k):
            q.popleft()
        # remove all smaller elements than current element
        while(len(q)!=0 and arr[q[-1]]<arr[i]):
            q.pop()
        # add current element to the deque
        q.append(i)
        # check from where to start adding to result
        if (i>=k-1):
            result[ind]=arr[q[0]]
            ind+=1
    return result