'''Dijkstra doesn’t work for Graphs with negative weight edges, Bellman-Ford 
works for such graphs as it can detect a negative cycle if the wiegts are changing 
even after continuing for (V-1) iterations.
Bellman Ford works on Dynamic Programming Approach
Time Complexity of Bellman-Ford is O(VE), which is more than Dijkstra.'''

class Graph:
	def __init__(self,nVertices):
		self.nVertices=nVertices
		self.graph=[]

	def addEdge(self,u,v,w):
		self.graph.append([u,v,w])

	# helper function to print shortest path from source vertex
	def printArr(self,dist):
		print("Shortest path from source to every vertex ")
		for i in range(self.nVertices):
			print(f'{i}\t\t{dist[i]}')

	def bellman(self,src):
		# initializing distances for every vertex to infinity
		dist=[float('inf')]*self.nVertices
		# distance of source vertex is made 0
		dist[src]=0
		# iterating for (V-1) times
		for _ in range(self.nVertices-1):
			for u,v,w in self.graph:
				# if dist for particular node is not infifniy and ashorter path is available 
				if dist[u]!=float('inf') and dist[u]+w<dist[v]:
					dist[v]=w+dist[u]
		# even after iterating for (V-1) times if distance changes the there is a negative cycle
		for u,v,w in self.graph:
			if dist[u]!=float('inf') and dist[u]+w<dist[v]:
				print('Negative cycle present')
		self.printArr(dist)

g = Graph(5) 
g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3) 
   
g.bellman(0)