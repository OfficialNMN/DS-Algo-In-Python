# To find min cost to reach the last cell in  a given 2d Array

def min_cost(arr,row,col):
	if row==-1 or col==-1:
		return float('inf')
	if row==0 and col==0:
		return arr[0][0]
	else:
		option1=min_cost(arr,row-1,col)
		option2=min_cost(arr,row,col-1)
		return arr[row][col]+min(option1,option2)
arr=[[4,7,8,6,4],
	[6,7,3,9,2],
	[3,8,1,2,4],
	[7,1,7,3,7],
	[2,9,8,9,3]]

print(min_cost(arr,4,4))