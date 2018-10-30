def cul(x,y):
    if x%2 == 0:
        return cul(int(x/2),y+1)
    else:
        return y

N = int(input())
A = list(map(int,input().split(" ")))
count = 0
for i in range(len(A)):
    count += cul(A[i],0)
print(count)
