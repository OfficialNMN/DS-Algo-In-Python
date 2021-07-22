from collections import defaultdict

# using BFS to detect cycle in the directed graph

class Graph:
	# using dict as adjacency list
	def __init__(self,vertices):
		self.graph=defaultdict(list)
		self.vertices=vertices

	def addEdge(self,v,w):
		self.graph[v].append(w)

	# using dfs approach to check whether a particular call is already is recursion stack or not 
	def dfs(self,graph,v,visited,recursionStack):
		visited[v]=True
		recursionStack[v]=True
		for adj in self.graph[v]:
			if (visited[adj]==False and self.dfs(graph,adj,visited,recursionStack)==True):
				return True
			elif (recursionStack[adj]==True):
				return True
		recursionStack[v]=False
		return False		 


	def is_cyclic(self):
		visited=[False]*self.vertices
		# used to maintain nodes that are currently in stack so that while 
		# checking if a node is already in recursion stack then it will indicate a cycle
		recursionStack=[False]*self.vertices
		for i in range(self.vertices):
			if visited[i]==False:
				if self.dfs(self.graph,i,visited,recursionStack) is True:
					return True
		return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)

print(g.graph)
print(g.is_cyclic())
