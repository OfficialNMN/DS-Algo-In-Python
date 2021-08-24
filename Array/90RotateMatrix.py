def ClockWiserotate(matrix):
    n=len(matrix)
    # taking transpose of matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    # reversing every row
    for i in range(n):
        matrix[i].reverse()

#  In case of anti-clock rotation reverse the whole matrix after transpose