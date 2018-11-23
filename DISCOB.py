N = int(input())
if N%2 == 1:
    N -= 2
    ans = N
    while(N != 1):
        N -= 2
        ans += N*2
    print(ans)
else:
    print((N**2)//2-N)
