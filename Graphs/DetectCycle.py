from collections import defaultdict

class Graph:
	# using dict as adjacency list
	def __init__(self,vertices):
		self.graph=defaultdict(list)
		self.vertices=vertices

	def addEdge(self,v,w):
		self.graph[v].append(w)

	def is_cyclic(self):
		visited=[False]*self.vertices
		for i in range(self.vertices):
			if visited[i]==False:
				if self.cyclic_util(self.graph,i,visited):
					return True
		return False

	def cyclic_util(self,graph,v,visited):
		queue=[v]
		while queue:
			res=queue.pop(0)
			if visited[res]==True:
				return True
			visited[res]=True
			for edge in self.graph[res]:
				if visited[edge]==False:
					queue.append(edge)
		return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(g.is_cyclic())
print(g.graph)