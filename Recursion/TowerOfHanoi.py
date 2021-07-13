# Tower Of Hanoi Problem using Recursion

def towerofhanoi(n,src,dest,helper):
	if n==0:
		return 
	# move n-1 discs from src to helper
	towerofhanoi(n-1,src,helper,dest)
	# moving the bottommost disc to dest from src
	print(f'Move {n} disc from {src} to {helper}')
	towerofhanoi(n-1,helper,dest,src) 

towerofhanoi(3,'A','B','C')