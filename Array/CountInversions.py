def merge(a1,a2,a):
	i=0
	j=0
	k=0
	inv=0
	while i < len(a1) and j < len(a2):
		if (a1[i] < a2[j]):
			a[k] = a1[i]
			k+=1
			i+=1
		else:
			a[k] = a2[j]
			k+=1
			j+=1
			inv+=len(a1)-i

	# To fill the leftover elements of the longer list		
	while i < len(a1):
		a[k]=a1[i]
		k+=1
		i+=1

	while j < len(a2):
		a[k] = a2[j]
		k+=1
		j+=1		

	return inv

def mergesort(a):
	if len(a)==0 or len(a)==1:
		return 
	mid=len(a)//2
	a1 = a[0:mid]
	a2 = a[mid:]
	mergesort(a1)
	mergesort(a2)
	return merge(a1,a2,a)

print(mergesort([2, 4, 1, 3, 5]))

