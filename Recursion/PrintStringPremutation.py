def printpermutations(ques,ans):
    if (len(ques)==0):
        print(ans)
        return 
    for i in range(len(ques)):
        c=ques[i]
        left=ques[:i]
        right=ques[i+1:]
        rest=''
        rest=left+right
        printpermutations(rest,ans+c)

printpermutations('abc','')