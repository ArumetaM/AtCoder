N = int(input())
count = 0
red = []
blue = []
for i in range(N):
    x,y = map(int,input().split(" "))
    red.append([x,y])
for i in range(N):
    x,y = map(int,input().split(" "))
    blue.append([x,y])
blue.sort()
for i in range(N):
    x = blue[i][0]
    y = blue[i][1]
    xy = []
    ymax = 0
    for j in range(N):
        if (red[j][0] < x)and(red[j][1] < y):
            xy.append(red[j])
    if len(xy) == 0:
        continue
    else:
        num = 0
        for j in range(len(xy)):
            if ymax < xy[j][1]:
                ymax = xy[j][1]
                num = j
        red[red.index(xy[num])] = [101,101]
        count += 1
print(count)
