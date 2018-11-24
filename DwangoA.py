N = int(input())
a = list(map(int,input().split(" ")))
b = sum(a) / N
now = 100
count = 0
for i in range(N):
    c = abs(a[i]-b)
    if now > c:
        count = i
        now = c
print(count)
