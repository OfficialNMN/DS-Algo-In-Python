def findPages(A, N, M):
    # if students are less than books
    if N<M:
        return -1
    low=min(A)
    high=sum(A)
    result=-1
    # our aim is to minimize the mid which allocates 
    # it to less than or equal to number of students
    while(low<=high):
        mid=(low+high)//2
        if allocation(A,N,M,mid):
            result=mid
            high=mid-1
        else:
            low=mid+1
    return result

# function to check whether pages can be alloted 
# to less than or equal to given number of students
def allocation(A,N,M,mid):
    student=1
    pages=0
    for i in range(N):
        if A[i]>mid:
            return False
        # if pages go out of mid then new student is required
        if (pages+A[i])>mid:
            student+=1
            pages=A[i]
            if student>M:
                return False
        else:
            pages+=A[i]
    return True