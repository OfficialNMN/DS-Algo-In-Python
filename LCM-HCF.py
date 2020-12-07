a=input('enter number 1: ')
b=input('enter number 2: ')

def gcd(a,b):
    gcd = 1
    for i in range(1,a+1):
        if (a%i==0 and b%i==0):
           gcd = i
    return gcd

lcm=(a*b)/gcd(a,b)
