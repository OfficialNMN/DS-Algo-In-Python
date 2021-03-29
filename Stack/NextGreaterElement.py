# To find next greater element for each number in the given array

def nextGreater(A):
	greater=[]
	for i in range(len(A)):
		found=False
		for j in range(i+1,len(A)):
			if A[i]<A[j]:
				found=True
				greater.append(A[j])
				break
		if found==False:
			greater.append(-1)

	return greater

print(nextGreater([4,5,2,10]))