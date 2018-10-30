import math

def makePrime(x):
    x = int(x)
    x += 1
    count = 0
    if x%5 != 1:
        x += 6-x%5
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i == 0:
            count = 1
            break
    if count == 1:
        return str(makePrime(x+1))
    else:
        return str(x)

N = int(input())
a = []
a.append(str(11))
for i in range(N-1):
    b = a[i]
    a.append(makePrime(b))
print(' '.join(a))
