import numpy as np

# To find whether a number is prime or not
# TimeComplexity--->O(sqrt(n))
def isprime(n):
	for i in range(2,int(np.sqrt(n))+1):
		if (n%i)==0:
			return False
	return True

# TimeComplexity---->O(n*sqrt(n))
def printPrime(n):
	for i in range(2,n+1):
		if (isprime(i)):
			print(i)

printPrime(10)

# SieveOfEratosthenes
# TimeComplexity---->O(n*log(log(n)))

def Sieve(n):
	# Create a boolean array "prime[0..n]" and initialize all entries it as true
	prime=[True for i in range(n+1)]
	p=2
	for p in range(2,int(np.sqrt(n))+1):
		# If prime[p] is True, then it is a prime
		if (prime[p]==True):
			# Update all multiples of p starting from its square
			for i in range(p*p,n+1,p):
				prime[i]=False
		p+=1

	# Print all prime numbers
	for p in range(2,n+1):
		if prime[p]:
			print(p)

# To find LCM(smallest divisible numbers) of all N numbers with input N
def lcm(N):
	ans=1
	for i in range(1,n+1):
		ans=(int(ans*i)/math.gcd(ans,i))
	return ans 

# To find GCD using Euclid's Algorithm
def gcd(a,b):
	# if divisor becomes 0 then return the dividend
	if b==0:
		return a
	# else recursively call function with 
	# dividend = divisor
	# divisor = remainder of a and b
	return gcd(b,a%b)

print(gcd(55,80))
