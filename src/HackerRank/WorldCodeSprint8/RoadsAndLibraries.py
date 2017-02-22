#!/bin/python3
import sys

class node:
    def __init__(self,data = None):
        self.data = data
        self.par = None
        self.rank = 0

class disjointset:
    def __init__(self):
        self.dic = {}
    def makeset(self,data):
        newNode = node(data)
        newNode.par = newNode
        self.dic[data] = newNode     
    def findset(self,Node):
        if Node.par == Node:
            return Node
        Node.par = self.findset(Node.par)
        return Node.par
    def union(self,x,y):
        Node1 = self.dic[x]
        Node2 = self.dic[y]        
        rep1 = self.findset(Node1)     
        rep2 = self.findset(Node2)
        if rep1.rank > rep2.rank:
            rep2.par = rep1
        else:
            rep1.par = rep2
            if rep1.rank == rep2.rank:
                rep2.rank = rep2.rank + 1    

q = int(input().strip())
for a0 in range(q):
    n,m,x,y = input().strip().split(' ')
    n,m,x,y = [int(n),int(m),int(x),int(y)]
    edges = []
    
    for a1 in range(m):
        city_1,city_2 = input().strip().split(' ')
        edges.append((int(city_1),int(city_2)))
    
    if x <= y:
        print(n*x)
    else:
        ds = disjointset()
        for i in range(1,n+1):
            ds.makeset(i)
        for i in range(0,m):
            ds.union(edges[i][0],edges[i][1])
        
        rep = []
        for i in range(1,n+1):
            rep.append(ds.findset(ds.dic[i]).data)
        
        repdic = {i:0 for i in rep}
        for i in rep:
            repdic[i] = repdic[i] + 1
        
        mincost = 0
        for i in repdic.keys():
            mincost = mincost +(repdic[i]-1)*y + x
        
        print(mincost) 
