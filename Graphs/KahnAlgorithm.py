'''Kahn's Algorithm is used for topological sort in which

1. in_degree of every node is calculated
2. all the nodes with in_degree=0 are added to queue
3. now one by one nodes are popped out of queue and added to answer array
4. for each popped node, in_degree of all its adjacent nodes is decreased by 1
5. now if any node's in_degree becomes 0, is added to queue
6. this continues till the queue becomes empty
'''

from collections import defaultdict

class Graph:
	# using dict as adjacency list
	def __init__(self,V):
		self.adjList=defaultdict(list)
		self.V=V

	def addEdge(self,vertex,edge):
		# creating adjacency list for directed graph
		self.adjList[vertex].append(edge)

	def topo_sort(self,v):
		in_degree=[0]*v
		for i in self.adjList:
			for j in self.adjList[i]:
				in_degree[j]+=1
		queue=[]
		for i in range(v):
			if in_degree[i]==0:
				queue.append(i)
		topo=[]
		while queue:
			node=queue.pop(0)
			topo.append(node)
			for i in self.adjList[node]:
				in_degree[i]-=1
				if in_degree[i]==0:
					queue.append(i)
		return topo

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print(g.topo_sort(6))

''' We can create a variable to count the visited nodes & if at the end of algorithm 
visited nodes != total graph node, this concludes that the graph contains a cycle bcoz, topo sort is only 
generated for directed acyclic graphs.
'''