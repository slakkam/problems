
t = int(input())
import math


for _ in range(t):
    n = int(input())
    laddersDic = {}
    
    for _ in range(n):
        edge = [int(i) for i in input().split()]
        laddersDic[edge[0]] = edge[1]
    
    m = int(input())
    snakesDic = {}
    for _ in range(m):
        edge = [int(i) for i in input().split()]
        snakesDic[edge[0]] = edge[1]
        
    queue = []
    queue.append(1)
    flag = False
    noLoops = 0
    visited = [1]
    parent = {}
    
    while len(queue) > 0:
        
        front = queue.pop(0)        

        for i in range(1,7):
            currentCell = front + i
            if currentCell in laddersDic:
                currentCell = laddersDic[currentCell]
            elif currentCell in snakesDic:
                currentCell = snakesDic[currentCell]
            
            if currentCell not in visited:
                queue.append(currentCell)
                visited.append(currentCell)
                parent[currentCell] = front
            
            if currentCell == 100:
                flag = True
        #print(queue)
        if flag:
            break
    
    if 100 not in parent:
        print(-1)
    else: 
        temp = 100
        while True:
            noLoops += 1
            #print(temp)
            temp = parent[temp]
            if temp == 1:            
                break

        print(noLoops)
