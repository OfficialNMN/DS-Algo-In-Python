# Combination Sum I
def combinationalSum(A, B):
    A.sort()
    ans=[]
    temp=[]
    combinations(0,A,B,temp,ans)
    return ans

def combinations(ind,A,B,temp,ans):
    if B==0:
        ans.append(temp[:])
        return 
    for i in range(ind,len(A)):
        # to remove duplicates
        if (i!=ind and A[i]==A[i-1]):
                continue
        if (B>=A[i]):
            temp.append(A[i])
            # here i remains same since no unique combination is required
            combinations(i,A,B-A[i],temp,ans)
            temp.remove(A[i])

# Combination Sum II
# Here we have to find only unique combinations

def combinationSum(A, N, B):
    A.sort()
    ans=[]
    # used as data structure in every recursive call to store values
    c=[]
    combinations(0,A,B,ans,c)
    return ans

def combinations(ind, A, B, ans,c):
    # base case when target becomes 0
    if B==0:
        ans.append(c[:])
        return 
    
    # to check which element to pick
    for i in range(ind,len(A)):
        # to avoid duplicates
        # i>ind is to pick the first occurence
        if (i>ind and A[i]==A[i-1]):
            continue
        # since arr is sorted if a[i]>target next values cannot be picked
        if A[i]>B:
            break
        c.append(A[i])
        # recursive call for next i
        combinations(i+1,A,B-A[i],ans,c)
        c.pop()