def generate(numRows):
    result=[[1]]
    for r in range(2,numRows+1):
        # first element in a row is always 1
        temp=[1]
        for c in range(1,r-1):
            # middle element is sum of its above 2 elements
            temp.append(result[-1][c]+result[-1][c-1])
        # last element in a row is always 1
        temp.append(1)
        result.append(temp)
    return result