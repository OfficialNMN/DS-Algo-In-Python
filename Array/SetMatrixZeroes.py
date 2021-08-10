def setZeroes(matrix):
    M,N=len(matrix),len(matrix[0])
    # creating dummy row and col array of size M,N initialised to 1
    row=[1]*M
    col=[1]*N
    # updating the dummy array to 0 at index where matrix is 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j]==0:
                row[i]=0
                col[j]=0
    # updating rows of matrix
    for r in range(M):
        if row[r]==0:
            matrix[r]=[0]*N
    # updaing columns of matrix
    for c in range(N):
        if col[c]==0:
            for i in range(M):
                matrix[i][c]=0