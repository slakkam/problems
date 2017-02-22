n = int(input())
m = int(input())
matrix = [[int(i) for i in input().split()] for i in range(n)]

def valid(ver):
    if 0 <= ver[0] < n and 0 <= ver[1] < m and matrix[ver[0]][ver[1]]:
        return True
    else:
        return False

def DFS(matrix):
    visited = {}
    regions = []
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                visited[(i,j)] = True
            else:
                vertex = (i,j)
                if vertex not in visited:
                    regions.append(dfsTraversal(matrix, vertex, visited,count = [0]))
    return max(regions)


def dfsTraversal(matrix, vertex, visited, count):
    count[0] += 1
    visited[vertex] = True
    i,j = vertex
    adj = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
    
    #adjVer contains valid adjacent vertices
    adjVer = []
    for ver in adj:
        if valid(ver):
            adjVer.append(ver)
    
    for ver in adjVer:
        if ver not in visited:
            dfsTraversal(matrix, ver, visited, count)    
    return count[0]
    
print(DFS(matrix))  
