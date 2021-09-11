def celebrity(M, n):
    # assuming 0 as celebrity
    celeb=0
    # traversing in M if our assumed celebrity knows some i
    # then we update our celebrity = i 
    for i in range(1,n):
        if (M[celeb][i]==1):
            celeb=i
    # now we traverse over the new assumed celebrity
    # if that celebrity knows anyone
    # or if that celebrity is not known by even one, we return -1
    for i in range(n):
        if (i!=celeb and (M[i][celeb]==0 or M[celeb][i]==1)):
            return -1
    return celeb