# uses greedy approach on an undirected, connected and weighted graph

class Graph:
	def __init__(self,vertices,edges,nodes):
		self.edges=edges
		self.nodes=nodes
		self.vertices=vertices
		self.MST=[]

	def printMST(self):
		for start,dest,weight in self.MST:
			print(f"{start}->{dest}:{weight}")

	def prims(self):
		visited=[False]*(self.vertices)
		edgeNum=0
		visited[0]=True
		while edgeNum<self.vertices-1:
			min=float('inf')
			for i in range(self.vertices):
				if visited[i] == True:
					# searching for adjacent vertices
					for j in range(self.vertices):
						#  if adjacent vertex is not visited and there is an edge
						if ((not visited[j]) and self.edges[i][j]):
							if min>self.edges[i][j]:
								min=self.edges[i][j]
								start=i
								dest=j
			self.MST.append([self.nodes[start],self.nodes[dest],self.edges[start][dest]])
			visited[dest]=True
			edgeNum+=1
		self.printMST()

edges=[[0,10,20,0,0],
		[10,0,30,5,0],
		[20,30,0,15,6],
		[0,5,15,0,8],
		[0,0,6,8,0]]

nodes=['A','B','C','D','E']
g=Graph(5,edges,nodes)
g.prims()

