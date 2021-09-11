'''
1s compliment of x = ~x
2s compliment of x = -x = (~x)+1 
'''

'''
x << n means left shift i.e x will be multiplied by 2^n
x >> n means left shift i.e x will be divided by 2^n
'''

# To check whether power of 2 or not 
def isPowerofTwo(n):
    if n==0:
        return False
    elif n&(n-1)==0:
        return True
    return False

# To convert binary back to integer 
def BintoInt(s):
	return int(s,2)

# To convert binary to grey 
def binarytogreyConverter(n): 
	return n ^ (n >> 1)

# To convert grey to binary
def grayToBinary(n):
    binary=n
    while n>0:
        n=n>>1
        binary=binary^n
    return binary

