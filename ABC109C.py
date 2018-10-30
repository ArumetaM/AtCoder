import fractions
from functools import reduce

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

a = input()
N = int(a.split(" ")[0])
X = int(a.split(" ")[1])

place = list(map(int,input().split(" ")))

b = []
place.append(X)
place.sort()
for i in range(len(place)-1):
    b.append(int(place[i+1]) - int(place[i]))
print(gcd_list(b))
