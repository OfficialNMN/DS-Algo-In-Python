import DisjointSet as dst

class Graph:
	def __init__(self,vertices):
		self.vertices=vertices
		self.graph=[]
		self.nodes=[]
		self.MST=[]

	def addEdge(self,start,dest,weight):
		self.graph.append([start,dest,weight])

	def addNode(self,value):
		self.nodes.append(value)

	def printMST(self,start,dest,weight):
		for start, dest, weight in self.MST:
			print("%d - %d = %d" % (start, dest, weight))

	def kruskal(self):
		i,e=0,0
		ds=dst.DisjointSet(self.nodes)
		self.graph=sorted(self.graph,key=lambda item: item[2])
		while e<self.vertices-1:
			start,dest,weight= self.graph[i]
			i+=1
			x=ds.find(start)
			y=ds.find(dest)
			# checking that it does't cause cycle using disjoint set find function
			if x!=y:
				e+=1
				self.MST.append([start,dest,weight])
				ds.union(x,y)
		# to print weight of MST
		mincost=0
		for _,_,w in self.MST:
			mincost+=w
		print(mincost)
		self.printMST(start,dest,weight)

g = Graph(4)
g.addNode(0)
g.addNode(1)
g.addNode(2)
g.addNode(3)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.kruskal()