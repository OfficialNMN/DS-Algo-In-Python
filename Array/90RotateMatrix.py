mat=[[1,2,3],[4,5,6],[7,8,9]]
c=np.array(np.transpose(mat))

for j in range(len(c)):
	start=0
	end=len(c)-1
	while(start<end):
		c[start][j],c[end][j]=c[end][j],c[start][j]
		start+=1
		end-=1
print(c)