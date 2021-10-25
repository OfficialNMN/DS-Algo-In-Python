from collections import defaultdict

class Graph:
	# using dict as adjacency list
	def __init__(self,V):
		self.adjList=defaultdict(list)
		self.V=V

	def addEdge(self,vertex,edge):
		# creating adjacency list for undirected graph
		self.adjList[vertex].append(edge)
		self.adjList[edge].append(vertex)

	# Breadth First Search ----> O(V+E)
	def bfs(self,V):
		bfs=[]
		visited=[False]*(V)
		# creating an extra loop for unconnected graphs
		for i in range(V):
			if visited[i]!=1:
				# bfs code starts here
				queue=[]
				queue.append(i)
				visited[i]=True
				while queue:
					node=queue.pop(0)
					bfs.append(node)
					for adj in self.adjList[node]:
						if visited[adj]==False:
							queue.append(adj)
							visited[adj]=True
		return bfs

	# Depth Fist Search ----> O(V+E)
	def dfs(self, V):
		ans=[]
		visited=[False]*(V)
		for i in range(V):
			if visited[i]==False:
				# calling function will utilize stack
				self.dfsUtil(i,visited,ans)
		return ans
	
	def dfsUtil(self,node,visited,ans):
		ans.append(node)
		visited[node]=True
		for i in self.adjList[node]:
			if visited[i]==False:
				self.dfsUtil(i,visited,ans)


g=Graph(9)

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(1,4)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(4,5)
g.addEdge(6,7)
g.addEdge(6,8)

print(g.adjList)

print(g.bfs(9))
print(g.dfs(9))