'''Memoization means to store the value of a particular case and use it again later in program when needed to avoid the computation time again '''

''' Top Down Approach(Recursive) focuses on breaking down a big problem into smaller and understandable chunks '''

def fibonacci(n,memo):
	if n==0:
		return 0
	if n==1:
		return 1
	if n not in memo:
		memo[n]=fibonacci(n-1,memo)+fibonacci(n-2,memo)
	return memo[n]

my_dict={}
print(fibonacci(9,my_dict))


''' Bottom Up Approach(Tabulation) first focuses on solving the smaller problems at the fundamental level and then integrating them into a whole and complete solution '''

def fibTab(n):
	tb=[0,1]
	for i in range(2,n+1):
		tb.append(tb[i-1]+tb[i-2])
	return tb[n-1]
	
print(fibTab(5))
