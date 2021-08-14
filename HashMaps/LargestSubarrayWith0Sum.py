def maxLen(n, arr):
    # map to store every unique sum value
    dic={}
    max_len=0
    summ=0
    for i in range(n):
        summ+=arr[i]
        # if sum of subarray is 0 the increment the lenght
        if summ==0:
            max_len=i+1
        else:
            # if sum that exists in map is encountered again 
            # that means the subarray has 0 sum
            if summ in dic:
                # storing the max length 
                max_len=max(max_len,i-dic[summ])
            else:
                # if sum is encountered for first time then store in map
                dic[summ]=i
    return max_len