''' To find the maximum number of activities that can be done from the given number of activities '''

def activity(arr,n):
	selected=[]
	arr.sort(key=lambda x:x[2])
	i=0
	selected.append(arr[i][0])
	for j in range(1,n):
		if arr[j][1]>=arr[i][2]:          # if start time of next activity is greater or equal to finish of previous activity
			selected.append(arr[j][0])
			i=j
	return selected

print(activity([['A1',5, 9], ['A2',1, 2], ['A3',3, 4], ['A4',0, 6], ['A5',5, 7], ['A6',8, 9]],6))
