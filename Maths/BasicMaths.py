# To find whether a number is prime or not
# TimeComplexity----O(n)

def isprime(n):
	for i in range(2,n):
		if (n%i)==0:
			return False
	return True

# To find all prime numbers upto a given number

# Method 1.
# TimeComplexity----O(n*sqrt(n))

def PrintAllPrime(n):
	for i in range(2,n+1):
		if (isprime(i)):
			print(i)

# Method 2. SieveOfEratosthenes
# TimeComplexity----O(n*log(log(n)))

def Sieve(n):
	# Create a boolean array "prime[0..n]" and initialize all entries it as true
	prime=[True for i in range(n+1)]
	p=2
	while(p*p<=n):
		# If prime[p] is not changed, then it is a prime
		if (prime[p]==True):
			# Update all multiples of p
			for i in range(p*p,n+1,p):
				prime[i]=False
		p+=1

	# Print all prime numbers
	for p in range(2,n+1):
		if prime[p]:
			print(p)
