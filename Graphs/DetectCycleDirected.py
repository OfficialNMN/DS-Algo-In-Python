from collections import defaultdict

# using BFS to detect cycle in the directed adjList

class Graph:
	# using dict as adjacency list
	def __init__(self,v):
		self.adjList=defaultdict(list)
		self.v=v

	def addEdge(self,v,w):
		self.adjList[v].append(w)

	# using dfs approach to check whether a particular call is already is recursion stack or not 
	def dfs_cycle(self,adjList,v,visited,dfs_visited):
		visited[v]=True
		dfs_visited[v]=True
		for adj in self.adjList[v]:
			# if the node is not visited check it using dfs_cycle
			if (visited[adj]==False and self.dfs_cycle(adjList,adj,visited,dfs_visited)==True):
				return True
			# if node is visited then check dfs_visited array
			elif (dfs_visited[adj]==True):
				return True
		# when backtrack make visited in dfs_visited False
		dfs_visited[v]=False
		# no cycle detected
		return False		 


	def is_cyclic(self):
		visited=[False]*self.v
		# dfs_visited is used to check if a node is True both in visited and
		# dfs_visited, then it will indicate a cycle
		dfs_visited=[False]*self.v
		for i in range(self.v):
			if visited[i]==False:
				if self.dfs_cycle(self.adjList,i,visited,dfs_visited) is True:
					return True
		return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)

print(g.adjList)
print(g.is_cyclic())
