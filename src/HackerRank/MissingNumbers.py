n = int(input())
A = [int(i) for i in input().split()]

m = int(input())
B = [int(i) for i in input().split()]

count = [0 for _ in range(0,201)]


# decrement the values of count arr while reading from A
# increment the values of count arr while reading from B
pivot = A[0]
for i in range(n):
    count[A[i]-pivot+100] -= 1
    
for i in range(m):
    count[B[i]-pivot+100] += 1
    
for i in range(201):
    if count[i] > 0:
        print(i+pivot-100, end = ' ')
