#!/bin/python3

import sys

def A(x):
    # array A contains pattern
    a = x % 8
    if(a == 0 or a == 1): return x;
    if(a == 2 or a == 3): return 2;
    if(a == 4 or a == 5): return x+2;
    if(a == 6 or a == 7): return 0;

Q = int(input().strip())
for a0 in range(Q):
    L,R = input().strip().split(' ')
    L,R = [int(L),int(R)]
    #logic
    print(A(R)^A(L-1))
