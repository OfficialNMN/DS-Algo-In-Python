# To find next greater element for each number in the given array

def nextLargerElement(arr,n):
    stack=[arr[-1]]
    ans=[]
    # startinf from behind and appending those to stack
    for i in range(n-1,-1,-1):
    	# if smaller element in stack then pop it out 
        while(len(stack)!=0 and arr[i]>=stack[-1]):
            stack.pop()
        # if stack becomes empty -1 is the ans
        # otherwise the top of stack 
        if len(stack)==0:
            ans.append(-1)
        else:
            ans.append(stack[-1])
        # add every processed element to stack
        stack.append(arr[i])
    # reverse the ans since we traversed backwards
    ans.reverse()
    return ans

print(nextGreater([4,5,2,10]))
