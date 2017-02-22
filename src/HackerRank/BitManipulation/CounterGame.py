t = int(input().strip())

for i in range(0,t):
    N = int(input().strip())
    # see discussions for this cool trick
    noTurns = bin(N-1).count("1")
    
    if noTurns%2 == 0:
        print("Richard")
    else:
        print("Louise")
