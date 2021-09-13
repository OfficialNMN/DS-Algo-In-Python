# Roman To Integer
def romanToDecimal(S): 
    n=len(S)
    dic={'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    i=n-1
    output=0
    # traverse from back
    while i>=0:
        # for case when IV means 5-1=4
        if i<n-1 and dic[S[i]]<dic[S[i+1]]:
            output-=dic[S[i]]
        else:
            output+=dic[S[i]]
        i-=1
    return output

# Integer To Roman
def convertRoman(n):
    dic={'I': 1,
        'IV': 4,
        'V' : 5,
        'IX': 9,
        'X' : 10,
        'XL': 40,
        'L' : 50,
        'XC': 90,
        'C' : 100,
        'CD': 400,
        'D' : 500,
        'CM': 900, 
        'M' : 1000}
    roman=[]
    for k,v in reversed(dic.items()):
        while n>0:
            if v<=n:
                n-=v
                roman.append(k)
            else:
                break
    return "".join(roman)

print(convertRoman(5))