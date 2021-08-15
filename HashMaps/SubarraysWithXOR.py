from collections import defaultdict

def subarrayXOR(arr,k):
	mapp=defaultdict(int)
	mapp[0]=1
	count=0
	xor=0
	for i in arr:
		xor=xor^i
		if mapp[xor^k]:
			count+=mapp[xor^k]
		else:
			mapp[xor]+=1
	return count

print(subarrayXOR([4,2,2,6,4],6))