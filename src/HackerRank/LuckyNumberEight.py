#!/bin/python3

import sys
n = int(input().strip())
#n = 3
number = input().strip()
#number = 888
ar = [int(i) for i in str(number)]
dp = [[-1 for i in range(8)] for i in range(n)]
#print(ar)
#print(dp)
# your code goes here
for m in range(8):
    dp[n-1][m]=(1 if m==0 else 0)+(1 if (m*10+ar[n-1])%8==0 else 0)
if n>1:
    for i in range(n-2,-1,-1):
        for m in range(8):
            dp[i][m]=(dp[i+1][m]+dp[i+1][(m*10+ar[i])%8])%1000000007
ans = (dp[0][0]-1)% 1000000007
if ans >0 :
    print(ans)
else:
    print(0)
