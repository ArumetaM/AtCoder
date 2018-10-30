import statistics
N = int(input())
an = list(map(int,input().split(" ")))
for i in range(N):
    an[i] -= (i+1)
b = int(statistics.median(an))
an = list(map(lambda x:abs(x-b),an))
print(sum(an))
