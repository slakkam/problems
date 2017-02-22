#!/bin/python3

import sys
class Vertex:
    def __init__(self,data):
        self.data = data
        self.visited = False
        self.colour = "white"
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
            print(value.data,[node.data for node in value.adjVertices])
    def getVertex(self,data):
        return self.vertexDic[data]

cum_arr = [0]*100000
cum_arr[0] = 0
arr = [0]*100000
arr[0] = 0
for i in range(1,100000):
    cum_arr[i] = cum_arr[i-1] + i*(i+1)
    arr[i] = i*(i+1)
    
t = int(input().strip())
for a0 in range(t):
    n,m = [int(i) for i in input().split()]
    T = Tree()
    for i in range(1,n+1):
        T.addVertex(i)
    for i in range(m):
        edge = [int(i) for i in input().split()]
        fromV,toV = edge[0], edge[1]
        T.addEdge(fromV,toV)    
    # T.printTree()
    
    def DFS(T):
        componentsVertexCount = []
        for vertex in T.vertexDic.values():
            if not vertex.visited:
                # count: no of vertices in each traversal
                componentsVertexCount.append(dfsTraversal(T,vertex,count=[0],nonTreeEdges = [0]))
        return  componentsVertexCount     
    
    # dfsTraversal iterative version
    def dfsTraversal(T,vertex,count,nonTreeEdges):
        stack = []
        stack.append(vertex)        
        vertex.visited = True
        vertex.colour = "grey"        
        while len(stack) > 0:
            current_vertex = stack.pop()
            count[0] += 1
            current_vertex.colour = "black"
            for nbr in current_vertex.adjVertices:
                if nbr.visited and nbr.colour == "grey":
                    nonTreeEdges[0] += 1
                if not nbr.visited:
                    stack.append(nbr)
                    nbr.visited = True
                    nbr.colour = "grey"
        return (count[0],nonTreeEdges[0])

    componentsVertexCount = DFS(T)
    #print(componentsVertexCount)
    componentsTreeEdges = [ele[0]-1 for ele in componentsVertexCount]
    componentsNonTreeEdges = [ele[1] for ele in componentsVertexCount]
    
    TotalNonTreeEdges = sum(componentsNonTreeEdges)
    componentsTreeEdges.sort(reverse = True)
    
    ans = 0
    count = 0
    #print(componentsTreeEdges)
    for ele in componentsTreeEdges:        
        ans += cum_arr[ele] + ele*count
        count = count+arr[ele]
        #print(count)
    #print(TotalNonTreeEdges)
    ans +=  TotalNonTreeEdges*count
    
    print(ans)
