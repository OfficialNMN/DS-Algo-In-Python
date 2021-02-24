# Number of ways to express any number as a sum of 1,3,4 with repetitions allowed

def numberfactor(n):
	if n in [0,1,2]:
		return 1
	elif n==3:
		return 2
	else:
		sub1=numberfactor(n-1)
		sub2=numberfactor(n-3)
		sub3=numberfactor(n-4)
		return sub1+sub2+sub3

print(numberfactor(5))