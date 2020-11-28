def totalwater(arr,n):
	water=0
	for i in range(1,n-1):
		leftmax=arr[i]
		for j in range(i):
			leftmax=max(leftmax,arr[j])

		rightmax=arr[i]
		for j in range(i+1,n):
			rightmax=max(rightmax,arr[j])

		water=water+(min(leftmax,rightmax)-arr[i])

	return water

print(totalwater([3, 0, 2, 0, 4],5))

# TimeComplexity----O(n^2)
# SpaceComplexity---O(1)
