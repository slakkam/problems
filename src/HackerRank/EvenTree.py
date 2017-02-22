
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
        # self.vertexDic[fromV].adjVertices.append(self.vertexDic[toV])
        # for directed tree, following line is not required
        self.vertexDic[toV].adjVertices.append(self.vertexDic[fromV])
    def printTree(self):
        for value in self.vertexDic.values():
            print(value.data)
    def getVertex(self,data):
        return self.vertexDic[data]
        
if __name__ == '__main__':
    
    n,m = [int(i) for i in input().split()]
    
    T = Tree()
    for i in range(1,n+1):
        T.addVertex(i)
    for i in range(m):
        edge = [int(i) for i in input().split()]
        fromV,toV = edge[0], edge[1]
        T.addEdge(fromV,toV)    
    # T.printTree()
    
    
    count = 0 
    def size(T, root):
        rootNode = T.getVertex(root)
        if len(rootNode.adjVertices) == 0:
            return 1
        else:
            ans = 1
            for node in rootNode.adjVertices:
                ans += size(T,node.data)
            if ans%2 == 0:
                global count
                count += 1
            return ans
    
    size(T,1)
    print(count-1)
