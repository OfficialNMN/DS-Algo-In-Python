# An efficient approach for this problem is to use a binary search algorithm. 
# The idea is that for a number to be median there should be exactly (n/2) numbers 
# which are less than this number.
# So, we try to find the count of numbers less than all the numbers.

def numbers_lessthanEqual_mid(row,mid):
    l=0
    h=c-1
    while(l<=h):
        m=(l+h)//2
        if (row[m]<=mid):
            l=m+1
        else:
            h=m-1
    return l


def median(matrix, r, c):
	low=1
	high=1e9
	while(low<=high):
	    mid=(low+high)//2
	    # to store count of numbers less than or equal to mid
	    count=0
	    for i in range(r):
	        # counting for every row
	        count+=numbers_lessthanEqual_mid(matrix[i],mid)
	    # if median, there should be (r*c)/2 numbers smaller than median
	    if count<=(r*c)/2:
	        low=mid+1
	    else:
	        high=mid-1
    # low will be the answer
    return int(low)