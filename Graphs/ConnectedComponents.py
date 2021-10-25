from collections import defaultdict

# If number of components in graph = 1 then the graph is connected

class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def generateComponents(self,graph,src,comp,visited):
        visited[src]=True
        comp.append(src)
        for i in self.graph[src]:
            if visited[i]==False:
                self.generateComponents(self.graph,i,comp,visited)

    def componentUtil(self):
        components=[]
        visited=[False]*self.vertices
        for v in range(self.vertices):
            if visited[v]==False:
                comp=[]
                self.generateComponents(self.graph,v,comp,visited)
                components.append(comp)
        return components

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(2, 3)
g.addEdge(4, 5)
g.addEdge(5, 6)
g.addEdge(4, 6)

print(g.componentUtil())