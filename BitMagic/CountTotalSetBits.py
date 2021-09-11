def countSetBits(n):
    if n in [0,1]:
        return n
    x = largestpowerof2tilln(n)
    # counting set bits till latest power of 2 less than n
    count_till_2x = x*(1<<(x-1))
    # counting msb for numbers left
    msb = n-(1<<x)+1
    # after removing msb from them recursively calling function
    rest = n-(1<<x)
    count=count_till_2x+msb+countSetBits(rest)
    return count

# to check the largest power of 2 less than n
def largestpowerof2tilln(n):
    x=0
    while((1<<x)<=n):
        x+=1
    return x-1
