from collections import defaultdict

# using BFS to detect cycle in the graph
# Time Complexity - O(V+E)

class Graph:
	# using dict as adjacency list
	def __init__(self,v):
		self.adjList=defaultdict(list)
		self.v=v

	def addEdge(self,v,w):
		self.adjList[v].append(w)
		self.adjList[w].append(v)

	def is_cyclic(self):
		visited=[False]*self.v
		for i in range(self.v):
			if visited[i]==False:
				if self.cyclic_check(self.adjList,i,visited):
					return True
		return False

	def cyclic_check(self,adjList,v,visited):
		queue=[v]
		while queue:
			res=queue.pop(0)
			# this condition will occur when same node has been be visited twice from another path 
			if visited[res]==True:
				return True
			visited[res]=True
			for edge in self.adjList[res]:
				if visited[edge]==False:
					queue.append(edge)
		return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)

print(g.adjList)
print(g.is_cyclic())
