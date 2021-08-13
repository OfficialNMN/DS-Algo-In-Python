# Merging 2 sorted arrays without any extra space
# Time Complexity - O(mn) 

def merge(arr1,arr2):
	i=0
	while(i<len(arr1)):
		if arr1[i]>arr2[0]:
			# swapping arr1[i] with 1st element of arr2
			arr1[i],arr2[0]=arr2[0],arr1[i]
			# sorting arr2 after every swap
			insertionsort(arr2,0)
		i+=1

# using insertion 
def insertionsort(arr2,index):
	temp=arr2[index]
	index+=1
	while(index<len(arr2) and arr2[index]<temp):
		arr2[index-1]=arr2[index]
		index+=1
	arr2[index-1]=temp

c1=[2,3,8,13]
c2=[1,5,9,10,15,20]

merge(c1,c2)
