def coin_combination(coins,target):
	# array of coins, target is amount to be paid
	ways=[0 for _ in range(target+1)]
	ways[0]=1
	for i in range(len(coins)):
		for j in range(coins[i],target+1):
			ways[j]+=ways[j-coins[i]]
	return ways[-1]

print(coin_combination([2,3,5],7))

def coin_permutation(coins,target):
	ways=[0 for _ in range(target+1)]
	ways[0]=1
	for i in range(1,target+1):
		for j in range(len(coins)):
			ways[i]+=ways[i-coins[j]]
	return ways[-1]

print(coin_permutation([2,3,5],7))

