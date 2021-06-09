from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def allPaths(self,start,dest,visited,path):
        visited[start]=True
        path.append(start)
        if start==dest:
            print(path)
        else:
            for i in self.graph[start]:
                if visited[i]==False:
                    self.allPaths(i,dest,visited,path)
        path.pop()
        visited[start]=False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)

visited=[False]*g.vertices
path=[]
g.allPaths(2,3,visited,path)