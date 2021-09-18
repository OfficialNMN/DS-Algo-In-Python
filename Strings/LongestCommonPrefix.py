def longestCommonPrefix(arr):
    n=len(arr)
    # lcp will not be grater than len of smallest string
    minlen=len(arr[0])
    for i in range(1,n):
        minlen=min(len(arr[i]),minlen)
    # if no lcp found
    lcp=""
    for i in range(minlen):
        # character to be compared in each iteration
        curr=arr[0][i]
        for j in range(n):
            # if character does not match
            if arr[j][i]!=curr:
                return lcp
        # append the matching character
        lcp+=curr
    return lcp