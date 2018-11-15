N = int(input())
atime,ax,ay = 0,0,0
for i in range(N):
    btime,bx,by = map(int,input().split(" "))
    distance = abs(bx-ax)+abs(by-ay)
    time = btime-atime
    if (time >= distance)and((time-distance)%2 == 0):
        ax = bx
        ay = by
        atime = btime
    else:
        print('No')
        exit()
print('Yes')
