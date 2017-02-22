#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)
    
    def gridsearch():
        for i in range(0,R-r+1):
            for j in range(0,C-c+1):
                flag = True
                for k in range(0,r):
                    if G[i+k][j:j+c] != P[k]:
                        flag = False
                        break
                if flag:
                    return True
        return False
    
    print("YES" if gridsearch() else "NO")
