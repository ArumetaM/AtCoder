import copy
N,K = map(int,input().split(" "))
a = list(map(int,input().split(" ")))
b = [a[0]]
for i in range(N-1):
    b.append(b[i]+a[i+1])
c = copy.deepcopy(b)
for i in range(N-1):
    aa = a[i]
    for j in range(N-i-1):
        c.append(b[j+i+1]-aa)
ans = max(c)
if K == 1:
    print(ans)
else:
    c[c.index(max(c))] = 0
    for i in range(K-1):
        d = 0
        count = j
        for j in range(len(c)):
            aa = c[j] & ans
            if d < aa:
                d = aa
                count = j
        ans = d
        c[count] = 0
    print(ans)
