class Graph:
	# using dict as adjacency list
	def __init__(self,adjList=None):
		if adjList is None:
			adjList={}
		self.adjList=adjList

	def addEdge(self,vertex,edge):
		self.adjList[vertex].append(edge)

	# Breadth First Search ----> O(V+E)
	def bfs(self,start):
		visited=[start]
		queue=[start]
		while queue:
			v=queue.pop(0)
			print(v)
			for adjacent in self.adjList[v]:
				if adjacent not in visited:
					visited.append(adjacent)
					queue.append(adjacent)

	# Depth Fist Search ----> O(V+E)
	def dfs(self,start):
		visited=[start]
		stack=[start]
		while stack:
			v=stack.pop()
			print(v)
			for adjacent in self.adjList[v]:
				if adjacent not in visited:
					visited.append(adjacent)
					stack.append(adjacent)

custom={'a':['b','c'],
        'b':['a','d','e'],
        'c':['a','e'],
        'd':['b','e','f'],
        'e':['d','f'],
        'f':['d','e'],}

g=Graph(custom)

# g.bfs('a')
# g.dfs('a')
