A = int(input())
B = int(input())
C = int(input())
X = int(input())
count = 0

if A*500 > X:
    A = int(X/500)

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if X == 500*i+100*j+50*k:
                count += 1
print(count)
