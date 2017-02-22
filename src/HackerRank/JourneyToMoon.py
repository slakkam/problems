class Vertex:
    def __init__(self,data):
        self.data = data
        self.visited = False
        self.adjVertices = []

class Tree:
    def __init__(self):
        self.vertexDic = {}
        self.numVertices = 0
    def addVertex(self,data):
        newNode = Vertex(data)
        self.vertexDic[data] = newNode
        self.numVertices += 1
    def addEdge(self,fromV,toV):
        self.vertexDic[fromV].adjVertices.append(self.vertexDic[toV])
        # for directed tree, following line is not required
        self.vertexDic[toV].adjVertices.append(self.vertexDic[fromV])
    def printTree(self):
        for value in self.vertexDic.values():
            print(value.data)
        
if __name__ == '__main__':
    
    n,m = [int(i) for i in input().split()]
    
    T = Tree()
    for i in range(n):
        T.addVertex(i)
    for i in range(m):
        edge = [int(i) for i in input().split()]
        fromV,toV = edge[0], edge[1]
        T.addEdge(fromV,toV)    
    #T.printTree()
        
    def DFS(T):
        componentsVertexCount = []
        for vertex in T.vertexDic.values():
            if not vertex.visited:
                # count: no of vertices in each traversal
                componentsVertexCount.append(dfsTraversal(T,vertex,count=[0]))
        return  componentsVertexCount     
    
    def dfsTraversal(T,vertex,count):
        vertex.visited = True
        count[0] += 1
        if len(vertex.adjVertices) != 0:
            for nbr in vertex.adjVertices:
                if not nbr.visited:
                    dfsTraversal(T,nbr,count)
        return count[0]
    
    ans = 0
    componentsVertexCount = DFS(T)
    # print(componentsVertexCount)
    nC2 = n*(n-1)/2
    x = 0
    for ele in componentsVertexCount:
        x += ele*(ele-1)/2
    
    ans = int(nC2-x)
    print(ans)
