'''
This algo is used to count number of set bits in an efficient manner.
by doing x = x - Right most set bit till x!=0.

Right most set bit = (x & -x)
2s compliment of x = -x = (~x)+1 
'''

def kernighan(n):
	count=0
	while(n!=0):
		rsbm=n&-n
		n=n-rsbm
		count+=1
	return count

print(kernighan(7))