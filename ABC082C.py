import collections
count = 0
N = int(input())
a = list(map(int,input().split(" ")))
c = collections.Counter(a)
C = c.most_common()
for i in C:
    A = i[0]
    B = i[1]
    if A < B:
        count += B-A
    elif A == B:
        continue
    else:
        count += B
print(count)
