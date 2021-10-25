''' Bipartite graph means that no two adjacent nodes in a graph will have same color.
A graph with even length cycle or no cycle is always a bipartite graph.
'''

from collections import defaultdict

class Graph:
	# using dict as adjacency list
	def __init__(self,v):
		self.adjList=defaultdict(list)
		self.v=v

	def addEdge(self,v,w):
		self.adjList[v].append(w)
		self.adjList[w].append(v)
	
	def isBipartite(self,v):
		# at starting every node is uncolored
		colors=[-1]*(v)
		queue=[]
		# looping through all nodes for unconnected
		for i in range(v):
			# if uncolored
			if colors[i]==-1:
				# coloring ith node with color 0 and adding to queue
				queue.append([i,0])
				# updating colors array
				colors[i]=0
				while queue:
					p=queue.pop(0)
					# current node
					v=p[0]
					# color of current node
					c=p[1]
					# looping in adjacent nodes
					for j in self.adjList[v]:
						# if 2 adjacent have same color return False
						if colors[j]==c:
							return False
						# else if uncolored
						elif colors[j]==-1:
							# coloring with opposite color
							if c==1:
								colors[j]=0
							else:
								colors[j]=1
							queue.append([j,colors[j]])
		return True

g=Graph(4)

# created a graph with odd length cycle
g.addEdge(1,3)
g.addEdge(1,2)
g.addEdge(2,3)

print(g.adjList)

print(g.isBipartite(9))

