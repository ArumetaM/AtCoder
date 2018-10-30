def gcd(a, b):
  while b > 0:
    a, b = b, a%b
  return a

N,M = map(int,input().split(" "))
S = input()
T = input()
N = len(S)
M = len(T)
x = gcd(N,M)
y = int(N*M/x)

for i in range(x):
    if S[int(i*y/M)] == T[int(i*y/N)]:
        continue
    else:
        print(-1)
        exit()
print(y)
