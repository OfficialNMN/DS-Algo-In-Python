''' In DFS, we start from a vertex, we first print it and then recursively call DFS 
for its adjacent vertices. In topological sorting, we use a temporary stack.
We don’t print the vertex immediately, we first recursively call topological 
sorting for all its adjacent vertices, then push it to a stack. Finally, print 
contents of the stack. Note that a vertex is pushed to stack only when all of its 
djacent vertices are already in the stack. '''

from collections import defaultdict

# Time Complexity: O(V+E)
class Graph:
	def __init__(self,nVertices):
		self.adjList=defaultdict(list)
		self.nVertices=nVertices

	def addEdge(self,vertex,edge):
		self.adjList[vertex].append(edge)

	def topoUtil(self,v,visited,stack):
		visited[v]=True
		# do for all the vertices adjacent to this vertex
		for i in self.adjList[v]:
			if visited[i]==False:
				self.topoUtil(i,visited,stack)
		# add vertex to stack
		stack.append(v)

	def topologicalSort(self):
		visited=[False]*self.nVertices
		stack=[]
		# implement topoUtil on all non visited vertices recursively
		for i in range(self.nVertices):
			if visited[i]==False:
				self.topoUtil(i,visited,stack)
		# print in reverse order
		print(stack[::-1])

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g.topologicalSort()
