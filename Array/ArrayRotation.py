# TimeComplexity----O(n*d)
# SpaceComplexity----O(1)

def leftrotate(arr,d,n):
	for i in range(d):
		leftrotatebyone(arr,n)

def leftrotatebyone(arr,n):
	temp=arr[0]
	for i in range(n-1):
		arr[i]=arr[i+1]
	arr[n-1]=temp

def printarray(arr,n):
	for i in range(n):
		print(arr[i],end=' ')

arr=[1,2,3,4,5,6,7]
leftrotate(arr,2,7)
printarray(arr,7)