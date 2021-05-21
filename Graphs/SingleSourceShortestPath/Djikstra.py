from collections import defaultdict
import heapq as hq
''' Djikstra is used for (+/-)weighted directed/undirected graphs but not for 
negative cycle graphs implemented using Min-Heap to get shortest path

Since we are using heap here 
Time Complexity is --> O(ELogV)'''

class Graph:
	# using dict as adjacency list
	def __init__(self,nVertices):
		self.adjList=defaultdict(list)
		self.nVertices=nVertices

	def addEdge(self,vertex,edge,distance):
		self.adjList[vertex].append((edge,distance))
	
def djikstra(graph,src,dest):
	# heap to create a track of vertices with cost
	# heappop will return vertex with least cost
	heap=[]
	hq.heappush(heap,(0,src))
	path=[]
	while (len(heap)!=0):
		currcost,currvtx=hq.heappop(heap)
		path.append(currvtx)
		if currvtx==dest:
			print(f"Path from {src} to {dest} is {path} with {currcost}")
			break
		for neigh,neighcost in g.adjList[currvtx]:
			hq.heappush(heap,(currcost+neighcost,neigh))

g=Graph(6)
g.addEdge('a', 'b',2)
g.addEdge('a', 'c',5)
g.addEdge('b', 'c',6)
g.addEdge('b', 'd',1)
g.addEdge('b', 'e',3)
g.addEdge('c', 'f',8)
g.addEdge('d', 'e',4)
g.addEdge('e', 'g',9)
g.addEdge('f', 'g',7)

djikstra(g,'a','c')
# print(g.adjList)
