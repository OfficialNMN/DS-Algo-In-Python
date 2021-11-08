
def permutation(s):
    if len(s)==1:
        return [s]
    perms=permutation(s[1:])
    char=s[0]
    result=[]
    for c in perms:
        for i in range(len(c)+1):
            result.append(c[:i]+char+c[i:])
    result.sort()
    return result

print(permutation('ABC'))
