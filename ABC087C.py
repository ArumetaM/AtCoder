N = int(input())
A1 = list(map(int,input().split(" ")))
A2 = list(map(int,input().split(" ")))
if N == 1:
    print(A1[0]+A2[0])
    exit()
B1 = [A1[0]]
B2 = [A2[0]]
for i in range(N-1):
    B1.append(B1[i]+A1[i+1])
for i in range(N-1):
    B2.append(B2[i]+A2[i+1])
for i in range(N):
    if i == 0:
        ans = B1[0]+B2[N-1]
    else:
        aaa = B1[i] + B2[N-1] - B2[i-1]
        ans = max(ans,aaa)
print(ans)
