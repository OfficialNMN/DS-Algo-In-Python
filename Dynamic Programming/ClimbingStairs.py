''' A child is running up a staircase with n steps and can hop either 1 step, 
2 steps, or 3 steps at a time. Implement a method to count how many possible 
ways the child can run up the stairs.'''

''' we can interpret this problem as climbing down as ways will remain same in
both climb up and down'''

def climb(n):
	ways=[0]*(n+1)
	# way of going to 0 from 0 is 1 i.e do not move 
	ways[0]=1
	ways[1]=1
	ways[2]=2
	# using tabulation to predict for all other cases
	for i in range(3,n+1):
		ways[i]=ways[i-1]+ways[i-2]+ways[i-3]
	return ways[n]

print(climb(4))