def find3Numbers(self,A, n, X):
    A.sort()
    # to store result
    ans=[]
    # continuing till 3rd last since we require triplet
    for i in range(0,n-2):
        if ((i==0) or (i>0 and A[i]!=A[i-1])):
        	# creating 2 pointers for every i one at i+1 and other at end
            low=i+1
            high=n-1
            summ=X-A[i]
            while(low<high):
            	# if sum is found
                if (A[low]+A[high]==summ):
                    ans.append([A[i],A[low],A[high]])
                    # removing duplicate values
                    while(low<high and (A[low]==A[low+1])):
                        low+=1
                    while(low<high and (A[high]==A[high-1])):
                        high-=1
                    # incrementing both when sum is found
                    low+=1
                    high-=1
                # if sum is less then only increment low
                elif(A[low]+A[high]<summ):
                    low+=1
                # if sum is high decrement high as array is sorted
                else:
                    high-=1
    if len(ans)>=1:
        return 1
    return 0