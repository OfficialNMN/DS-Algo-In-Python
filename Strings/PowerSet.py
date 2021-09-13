import math

def AllPossibleStrings(s):
    # in this we try to place 0/1 on indices
    for num in range(int(math.pow(2,len(s)))):
        substr=""
        for i in range(len(s)):
           # to check at what indexes bit is 1 
            if (num&(1<<i))>0:
                substr+=s[i]
        print(substr)

AllPossibleStrings('abc')
