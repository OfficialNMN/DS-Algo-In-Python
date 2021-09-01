# Partition in such a way that returned strings are palindrome

def partition(s):
    result=[]
    path=[]
    palin_strings(0,s,path,result)
    return result

def palin_strings(index,s,path,result):
    if index==len(s):
        result.append(path[:])
        return
    for i in range(index,len(s)):
        if ispalindrome(s,index,i):
            path.append(s[index:(i+1)])
            palin_strings(i+1,s,path,result)
            path.pop()
    
def ispalindrome(s,start,end):
    return s[start:end+1]==s[start:end+1][::-1]

print(partition('aab'))