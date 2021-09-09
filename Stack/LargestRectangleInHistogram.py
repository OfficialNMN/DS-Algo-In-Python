# Basic Approach with O(4N) Time Complexity

def getMaxArea(histogram):
    n=len(histogram)
    left_small=[0 for i in range(n)]
    right_small=[0 for i in range(n)]
    stack=[]
    # find next smaller on left for a particular bar
    for i in range(n):
        # keep on popping form stack untill we get the next smaller on left side
        while(len(stack)!=0 and histogram[stack[-1]]>histogram[i]):
            stack.pop()
        if len(stack)==0:
            left_small[i]=0
        else:
            # boundary will be one greater than the index
            left_small[i]=stack[-1]+1
        stack.append(i)
    
    stack.clear()
    
    # find next smaller on right for a particular bar
    for i in range(n-1,-1,-1):
        # keep on popping from stack untill we get next smaller on right side
        while(len(stack)!=0 and histogram[stack[-1]]>histogram[i]):
            stack.pop()
        if len(stack)==0:
            right_small[i]=n-1
        else:
            # boundary will be one less than the index
            right_small[i]=stack[-1]-1
        stack.append(i)
    
    # to calculate are for every rectangle and then find max omong them
    maxarea=0
    for i in range(n):
        maxarea=max(maxarea,histogram[i]*(right_small[i]-left_small[i]+1))
    return maxarea

# Optimal Approach using Single Pass i.e. O(N)

def largestRectangleArea(histogram):
    stack=[]
    maxarea=0
    n=len(histogram)
    # in this method the stack will tell us the
    # left smaller and right smaller for particular bar height
    for i in range(n+1):
        # while value at top of stack >= current bar height
        while(len(stack)!=0 and ((i==n) or histogram[stack[-1]]>=histogram[i])):
            # height will be the top of stack which is the right smaller
            height=histogram[stack[-1]]
            stack.pop()
            # width = i if stack is empty 
            if len(stack)==0:
                width=i
            # else width is i-indexofrightsmaller-1
            else:
                width=i-stack[-1]-1
            maxarea=max(maxarea,width*height)
        # append at top 
        stack.append(i)
    return maxarea