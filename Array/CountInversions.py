def inversionCount(a, n):
    temp=[0]*n
    return self.mergesort(a,temp,0,n-1)

# using Enhanced Merge-Sort
def merge(a,temp,left,mid,right):
	# start index of left subarray
	i=left
	# start index of right subarray
	j=mid+1
	# start index of temp subarray
	k=left
	inv=0
	while i <= mid and j <= right:
		# No inversion if arr[i] <= arr[j]
		if (a[i] <= a[j]):
			temp[k] = a[i]
			k+=1
			i+=1
		else:
			# inversion will occur
			temp[k] = a[j]
			k+=1
			j+=1
			inv+=(mid-i+1)

	# copying the remaining elements
	while i <= mid:
		temp[k]=a[i]
		k+=1
		i+=1

	# copying the remaining elements
	while j <= right:
		temp[k] = a[j]
		k+=1
		j+=1	
	
	for var in range(left,right+1):
	    a[var]=temp[var]
	return inv

def mergesort(a,temp,left,right):
    inv=0
    if left<right:
        mid=(left+right)//2
        # inversions in left array
	    inv+=mergesort(a,temp,left,mid)
	    # inversions in right subarray
	    inv+=mergesort(a,temp,mid+1,right)
	    # merge 2 sorted subarrays
	    inv+=merge(a,temp,left,mid,right)
	return inv