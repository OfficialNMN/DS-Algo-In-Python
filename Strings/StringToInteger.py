def myAtoi(s):
    # removing whitespaces
    s=s.strip()
    # if s is null
    if not s:
        return 0
    # to check whether negative or positive
    neg=False
    res=0
    # checking sign 
    if s[0]=='-':
        neg=True
    elif s[0]=='+':
        neg=False
    # if first digit is not numeric
    elif not s[0].isnumeric():
        return 0
    # else converting string to number 
    else:
        res=ord(s[0])-ord('0')
    for i in range(1,len(s)):
        if s[i].isnumeric():
            res = res*10 + ord(s[i])-ord('0')
            # if result is out of bound [-2^31 to 2^31]
            if not neg and res >=2147483647:
                return 2147483647
            if neg and res >= 2147483648:
                return -2147483648
        # if a string is encountered
        else:
            break
    if not neg:
        return res
    else:
        return -res