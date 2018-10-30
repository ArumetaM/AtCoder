N = int(input())
c6 = 0
n6 = N
c9 = 0
n9 = N

for i in range(7):
    c6 += n6 % 6**(i+1)
    print(n6 % 6**(i+1),c6,n6)
    n6 -= (n6 % 6**(i+1))*(6**i)
for i in range(7):
    c9 += n9 % 9**(i+1)
    print(c9 % 9**(i+1),c9,n9)
    c9 -= (n9 % 9**(i+1))*(9**i)
print(min(c6,c9))
