''' In DFS, we start from a vertex, we first print it and then recursively call DFS 
for its adjacent vertices. In topological sorting, we use a temporary stack.
We don’t print the vertex immediately, we first recursively call topological 
sorting for all its adjacent vertices, then push it to a stack. Finally, print 
contents of the stack. Topological sort occurs in directed acyclic graphs only. '''

from collections import defaultdict

# Time Complexity: O(V+E)
class Graph:
	def __init__(self,vertices):
		self.adjList=defaultdict(list)
		self.vertices=vertices

	def addEdge(self,vertex,edge):
		self.adjList[vertex].append(edge)

	def topo_sort(self,v):
		visited=[False]*v
		stack=[]
		# implement topoSort on all non visited vertices recursively
		for i in range(v):
			if visited[i]==False:
				self.topo_util(i,visited,stack)
		# print in reverse order
		return stack[::-1]

	def topo_util(self,v,visited,stack):
		visited[v]=True
		# do for all the vertices adjacent to this vertex
		for i in self.adjList[v]:
			if visited[i]==False:
				self.topo_util(i,visited,stack)
		# add vertex to stack
		stack.append(v)

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print(g.topo_sort(6))

