def stockspan(price):
	span=[0 for i in range(len(price))]
	span[0]=1
	stack=[]
	stack.append(0)
	# start iterating from 2nd stock since span of 1st is already 1
	for i in range(1,len(price)):
		# continue till stack has elements and price[i]>price of stock at top of stack
		while(len(stack)>0 and price[i]>=price[stack[-1]]):
			stack.pop()
		# if stack is empty append the current i+1
		if len(stack)==0:
			span[i]=i+1
		else:
		# append i-top of stack
			span[i]=(i-stack[-1])
		stack.append(i)
	return span

print(stockspan([10,4,5,90,120,80]))