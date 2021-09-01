# we have to find nth root of a number m

def NthRoot(n, m):
	low=1
	high=m
    # using binary search 
	while(low<=high):
	    mid=(high+low)//2
	    x=math.pow(mid,n)
	    if x==m:
	        return mid
	    # if number calculated is less than m  
	    elif (x<m):
	        low=mid+1
	    # if number calculated is more than m 
	    else:
	        high=mid-1
    # if no perfect nth root is found
    return -1