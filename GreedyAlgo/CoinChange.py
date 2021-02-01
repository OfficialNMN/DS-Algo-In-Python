''' Problem here is to get the money in minimum number of coins '''

# TimeComplexity - O(n)

def coinchange(coins,N):
	coins.sort()
	index = len(coins)-1
	while True:
		coinvalue = coins[index]
		if N >= coinvalue:                 # if N > greatest coin then subtract that coin from N
			print(coinvalue)
			N = N-coinvalue
		if N < coinvalue:                  # if N < greatest coin then choose next greatest 
			index -= 1
		if N == 0:
			break

coinchange([1,2,5,20,50,100],201)
		

