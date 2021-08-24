# TimeComplexity----O(n*d)
# SpaceComplexity----O(1)

def leftrotate(arr,d,n):
	for i in range(d):
		leftrotatebyone(arr,n)
	return arr

def leftrotatebyone(arr,n):
	temp=arr[0]
	for i in range(n-1):
		arr[i]=arr[i+1]
	arr[n-1]=temp


arr=[1,2,3,4,5,6,7]
print(leftrotate(arr,2,7))

# Juggling Algorithm

# TimeComplexity---O(n)
# SpaceComplexity---O(1)

def rotateArr(self,arr,d,n):
	# reverse first d elements
    self.reverse(arr,0,d-1)
    # revrse d to last elements
    self.reverse(arr,d,n-1)
    # revrse the whole array
    self.reverse(arr,0,n-1)
    return arr
    
def reverse(self,arr,low,high):
    while(low<high):
    	# keep on swapping first with last in the given array
        arr[low],arr[high]=arr[high],arr[low]
        low+=1
        high-=1




