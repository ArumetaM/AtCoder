N,M = map(int,input().split(" "))
p = list(map(int,input().split(" ")))
xy = []
for i in range(M):
    aa = input().split(" ")
    x = int(aa[0])
    y = int(aa[1])
    xy.append([x,y])
link = []
linklist = []
for i in range(M):
    x = xy[i][0]
    y = xy[i][1]
    if (x not in linklist)and(y not in linklist):
        #一度も出現していないので新たなに枝を作成
        linklist.append(x)
        linklist.append(y)
        link.append(xy[i])
    elif (x in linklist)and(y in linklist):
        #枝と枝を結ぶ
        for j in range(len(link)):
            if x in link[j]:
                Xnode = link[j]
                break
        for j in range(len(link)):
            if y in link[j]:
                Ynode = link[j]
                break
        if Xnode == Ynode:
            continue
        else:
            new = Xnode+Ynode
            link.append(new)
            link.remove(Xnode)
            link.remove(Ynode)
    else:
        #枝を広げる
        for j in range(len(link)):
            if x in link[j]:
                link[j].append(y)
                linklist.append(y)
                break
            if y in link[j]:
                link[j].append(x)
                linklist.append(x)
                break
count = 0
for i in range(len(p)):
    if p[i] == (i+1):
        count += 1
    elif p[i] not in linklist:
        continue
    else:
        for j in range(len(link)):
            if (p[i] in link[j])and((i+1) in link[j]):
                count += 1
print(count)
