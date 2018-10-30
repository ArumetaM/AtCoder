input = input()
N = int(input.split(" ")[0])
Y = int(input.split(" ")[1])

if (Y < 1000*N) and (10000*N < Y):
    print(-1,-1,-1)
    exit()

for i in range(N+1):
    if Y-10000*i-5000*(N-i) > 0:
        continue
    for j in range(N-i+1):
        if (Y == i*10000+(N-i-j)*5000+(N-i-(N-i-j))*1000)and(i>=0)and(j>=0)and((N-i-j)>=0):
            print(i,(N-i-j),(N-i-(N-i-j)))
            exit()
        elif Y > i*10000+(N-i-j)*5000+(N-i-(N-i-j))*1000:
            break

print(-1,-1,-1)
