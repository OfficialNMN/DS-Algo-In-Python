'''Memoization means to store the value of a particular case and use it again 
ater in program when needed to avoid the computation time again '''

''' Top Down Approach(Recursive+Memoized) focuses on breaking down a big problem into 
smaller and understandable chunks '''

def Memofib(n,memo):
	if n==0 or n==1:
		return n
	if n not in memo:
		memo[n]=Memofib(n-1,memo)+Memofib(n-2,memo)
	return memo[n]

mydict={}
print(Memofib(9,mydict))

''' Bottom Up Approach(Tabulation) first focuses on solving the smaller 
problems at the fundamental level and then integrating them into a whole and 
complete solution '''

def fibTab(n):
	tb=[0,1]
	for i in range(2,n+1):
		tb.append(tb[i-1]+tb[i-2])
	return tb[n]
	
print(fibTab(9))