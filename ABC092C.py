N = int(input())
A = list(map(int,input().split(" ")))
A.append(0)
SUM = abs(A[0])
for i in range(N):
    SUM += abs(A[i+1]-A[i])
ans = SUM - abs(A[0]) - abs(A[1]-A[0]) + abs(A[1])
print(ans)
for i in range(1,N):
    ans  = SUM - abs(A[i]-A[i-1]) - abs(A[i+1]-A[i]) + abs(A[i+1]-A[i-1])
    print(ans)
