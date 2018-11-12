N = int(input())
s = []
for i in range(N-1):
    C,S,F = map(int,input().split(" "))
    s.append([C,S,F])
for i in range(N):
    if i == N-1:
        print(0)
    else:
        time = 0
        for j in range(i,N-1):
            C,S,F = s[j]
            if time < S:
                time = S + C
            else:
                if (time-S)%F == 0:
                    time += C
                else:
                    time += (F - (time-S)%F)
                    time += C
        print(time)
