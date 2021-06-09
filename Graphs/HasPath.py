class Graph:
    # using dict as adjacency list
    def __init__(self,nVertices):
        self.adjList=defaultdict(list)
        self.nVertices=nVertices

    def addEdge(self,vertex,edge):
        self.adjList[vertex].append(edge)

    def hasPath(self,src,dest):
        visited=[False]*(self.nVertices)
        queue=[]
        queue.append(src)
        visited[src]=True
        while queue:
            n=queue.pop(0)
            if n==dest:
                return True
            else:
                for i in self.adjList[n]:
                    if visited[i] is False:
                        queue.append(i)
                        visited[i]=True
        return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
        
print(g.hasPath(3,1))