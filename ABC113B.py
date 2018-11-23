N = int(input())
T,A = map(int,input().split(" "))
H = list(map(int,input().split(" ")))
ans = []
for i in range(N):
    H[i] = T - H[i]*0.006
    ans.append(abs(H[i]-A))
print(ans.index(min(ans))+1)
