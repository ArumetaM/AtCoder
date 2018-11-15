"""
import math
X,Y = map(int,input().split(" "))
print(int(math.log((Y/X),2)+1))
"""
X,Y = map(int,input().split(" "))
ans = 0
while X <= Y:
    ans += 1
    X *= 2
print(ans)
