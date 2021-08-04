# Quick Sort is an unstable in-place sorting algorithm

# Lomuto partition takes the last element of the unsorted array and places it in 
# correct place i.e. smaller element to its left and greater ones to right 

# More Efficient-->Hoare partition sets first element as pivot and then arranges elements such that all
# all smaller elements are to left and all greater are to right

def partition(a,low,high):
	pivot=a[low]
	i=low-1
	j=high+1
	while True:
		i+=1
		while (a[i]<pivot):
			i+=1

		j-=1
		while(a[j]>pivot):
			j-=1

		if (i>=j):
			return j
		a[i],a[j]=a[j],a[i]


def quick_sort(a,low,high):
	if low >= high:
		return
	pivot_index = partition(a,low,high)
	quick_sort(a,low,pivot_index)
	quick_sort(a,pivot_index+1,high) 

a=[4,3,5,1,2,9]
quick_sort(a,0,len(a)-1)
print(a)

