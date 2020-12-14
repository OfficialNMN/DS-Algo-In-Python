# To check whether power of 2 or not
def ispowerof2(n):
    if n <= 0:
        return False
    x = n
    y = not(n & (n-1))
    return x and y



# To count number of bits in a binary number
def count_bits(n):
	s=str(bin(5))[2:]
	return s.count('1')
