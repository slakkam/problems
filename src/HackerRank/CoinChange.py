
n,m = [int(i) for i in input().strip().split(' ')]
coins = [int(i) for i in input().strip().split(' ')]

def numWays(coins,m,n):   
    table = []
    for i in range(0,m):
        foo = [0 for j in range(0,n+1)]
        table.append(foo)
    
    for i in range(0,m):
        table[i][0] = 1
    
    for i in range(1,n+1):
        for j in range(0,m):
            #Count of solutions including coins[j]
            x = table[j][i-coins[j]] if (i-coins[j])>=0 else 0
            #Count of solutions excluding coins[j]
            y = table[j-1][i] if j>=1 else 0
            table[j][i] = x+y
    
    return(table[m-1][n])

print(numWays(coins,m,n))
