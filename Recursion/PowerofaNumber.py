def myPow(x, n):
    if n==0:
        return 1
    temp=myPow(x,int(n/2))
    # when n is even
    if n%2==0:  
        return temp*temp
    # when n<0
    elif n<0:
        return myPow((1/x),-n)
    # when n is odd
    else:
        return x*temp*temp