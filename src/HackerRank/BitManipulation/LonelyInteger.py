#!/usr/bin/py

# Head ends here
def lonelyinteger(b):
    answer = 0
    array = [0 for i in range(0,100)]
    
    for i in range(0,len(b)):
        array[b[i]] = array[b[i]] + 1
    for i in range(0,100):
        if array[i]==1:
            answer = i
            break
    return answer

# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = [int(i) for i in input().strip().split(" ")]
    print(lonelyinteger(b))
