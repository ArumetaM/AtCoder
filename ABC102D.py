N = int(input())
A = list(map(int,input().split(" ")))
B = [A[0]]
ans = []
for i in range(N-1):
    B.append(B[i]+A[i+1])
for i in range(1,N-2):
    BC = 10000000000
    ifB = 0
    ifC = 0
    for j in range(i):
        left = B[j]
        right = B[i] - left
        x = abs(right-left)
        if BC > x:
            BC = x
            ifB = left
            ifC = right
        else:
            break
    DE = 10000000000
    ifD = 0
    ifE = 0
    for j in range(i+1,N-1):
        left = B[j] - B[i]
        right = B[N-1] - B[j]
        x = abs(right-left)
        if DE > x:
            DE = x
            ifD = left
            ifE = right
        else:
            break
    ans.append(max(ifB,ifC,ifD,ifE)-min(ifB,ifC,ifD,ifE))
print(min(ans))
