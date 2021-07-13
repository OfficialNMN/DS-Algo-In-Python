def check(a,n):
	if n==1:
		return True
	if ((a[0]<a[1]) and (check(a[1:],n-1))):
		return True
	return False

print(check([1,2,13,4,5],5))