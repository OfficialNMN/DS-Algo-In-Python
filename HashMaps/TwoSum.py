# Find 2 elements that sum up to a given number in a given array using hashmaps

def keypair(A, N, X):
	hashmap=set()
	for i in range(N):
		temp=X-A[i]
		if temp in hashmap:
			return True
		else:
			hashmap.add(A[i])
	return False

print(keypair([1, 4, 45, 6, 10, 8],6,16))