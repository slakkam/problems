#!/bin/python3

import sys
n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
# your code goes here

mod_scores = list(set(scores))
mod_scores.sort(reverse=True)

pos = len(mod_scores)+1
for i in range(0,m):   
    flag = True
    if pos > 1:
        for j in range(pos-2,-1,-1):
            if alice[i] < mod_scores[j]:
                pos = j+2
                flag = False
                print(pos)
                break
    if flag:
        print(1)
