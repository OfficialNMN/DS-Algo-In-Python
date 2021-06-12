arr= [[ 0, 0, 1, 1, 1, 1, 1, 1],
     [ 0, 0, 1, 1, 1, 1, 1, 1],
     [ 1, 1, 1, 1, 1, 1, 1, 0],
     [ 1, 1, 0, 0, 0, 1, 1, 0],
     [ 1, 1, 1, 1, 0, 1, 1, 0],
     [ 1, 1, 1, 1, 0, 1, 1, 0],
     [ 1, 1, 1, 1, 1, 1, 1, 0],
     [ 1, 1, 1, 1, 1, 1, 1, 0]]

def getcomponent(arr,i,j,visited):
	if (i<0 or j<0 or i>=len(arr) or j>=len(arr[0]) or arr[i][j]==1 or visited[i][j]==True):
		return
	visited[i][j]=True
	getcomponent(arr,i-1,j,visited)
	getcomponent(arr,i,j+1,visited)
	getcomponent(arr,i,j-1,visited)
	getcomponent(arr,i+1,j,visited)

visited=[[False for _ in range(len(arr[0]))] for _ in range(len(arr))]
count=0

for i in range(len(arr)):
	for j in range(len(arr[i])):
		if arr[i][j]==0 and visited[i][j]==False:
			getcomponent(arr,i,j,visited)
			count+=1
print(count)



