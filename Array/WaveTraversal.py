import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)

# Wave Traversal
def wave(A):
    for i in range(len(A[0])):
        # when column is odd row increases
        if i%2==0:
            for j in range(len(A)):
                print(A[j][i])
        # when column is even row decreases
        else:
            for j in range(len(A)-1,-1,-1):
                print(A[j][i])
wave(twoDArray)