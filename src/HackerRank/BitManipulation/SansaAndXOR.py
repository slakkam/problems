
# Even N => 0 Odd N => XOR of elements at position 0,2,4,..... Easiest Solution.

#Reason:
#The number of occurance of an element can be given as 
#Total_i=(N-i)*(i+1) 
#(N-i) ==> Because the elements satrting postion. 
#(i+1) ==> Because the number of times to be repeated from previos elements.
#if the array is indexed from i=0 to N-1.

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().strip().split(" ")]
    
    if n%2 == 0:
        print(0)
    else:
        ans = arr[0]
        i = 2
        while i < n:
            ans = ans ^ arr[i]
            i += 2
        print(ans)
