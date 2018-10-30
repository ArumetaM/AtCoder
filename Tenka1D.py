import math
N = int(input())
M = 1/2 + math.sqrt(4*N+1)/2

if M%1 != 0:
    print("No")
else:
    print("Yes")
    M = int(M)
    print(M)
    Ans = [ [M-1] * M ]
