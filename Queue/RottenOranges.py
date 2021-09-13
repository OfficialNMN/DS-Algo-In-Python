def orangesRotting(grid):
	rows=len(grid)
	cols=len(grid[0])
	# all rotten will be pushed into queue and operated
	queue=[]
	total=0
	# traversing the matrix
	for i in range(rows):
	    for j in range(cols):
	    	# if orange is rotten add it to queue
	        if grid[i][j]==2:
	            queue.append((i,j))
	        # else increase count of total
	        if grid[i][j]!=0:
	            total+=1
	# if no orange present return 0
	if total==0:
	    return 0
	# to track rotten and time 
	time=0
	rotten=0
	dx=[0,0,1,-1]
	dy=[1,-1,0,0]
	while len(queue)!=0:
	    size=len(queue)
	    # rotten will be same as size of queue
	    rotten+=size
	    for i in range(size):
	    	# position of popped orange
	        posi=queue.pop(0)
	        # rotting all 4 directions
	        for j in range(4):
	            x=posi[0]+dx[j]
	            y=posi[1]+dy[j]
	            # to check if boundary and other constraints satisfied
	            if (x<0 or y<0 or x>=rows or y>=cols or grid[x][y]==0 or grid[x][y]==2):
	                continue
	            # rot that orange and push to queue
	            grid[x][y]=2
	            queue.append((x,y))
	    if len(queue)!=0:
	        time+=1
	# if at end rotten==total return time
	if total==rotten:
	    return time
	# else all did not get rotten return -1
	else:
	    return -1