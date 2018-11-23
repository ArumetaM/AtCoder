import collections
N,K = map(int,input().split(" "))
A = list(map(int,input().split(" ")))
count = collections.Counter(A)
num = len(count)-K
a = sorted(count.values())
print(sum(a[:num]))
