N = int(input())
mochi = []
count = 0

for i in range(N):
    x = int(input())
    if x not in mochi:
        count += 1
        mochi.append(x)

print(count)
