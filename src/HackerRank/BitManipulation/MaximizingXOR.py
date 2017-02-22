#!/usr/bin/python3

def maxXor(l, r):
    maxvalue = 0
    for a in range(l,r+1):
        for b in range(a,r+1):
            if a^b >= maxvalue:
                maxvalue = a^b
    return maxvalue

if __name__ == '__main__':
  l = int(input())
  r = int(input())
  print(maxXor(l, r))
