''' To find in how many cases a number can be represented as a sum of 1,3,4 with repetititons allowed '''

# TopDown approach
def NumberFactor(n,tb):
	if n in [0,1,2]:
		return 1
	elif n==3:
		return 2                          # 3 = {1,1,1},{3}
	else:
		if n not in tb:
			sub1=NumberFactor(n-1,tb)
			sub2=NumberFactor(n-3,tb)
			sub3=NumberFactor(n-4,tb)
			tb[n]=sub1+sub2+sub3
		return tb[n]

print(NumberFactor(5,{}))


# BottomUp Approach
def NumberFactor(n):
	factor=[1,1,1,2]
	for i in range(4,n+1):
		factor.append(factor[n-1]+factor[n-3]+factor[n-4])
	return factor[n]

print(NumberFactor(5))
