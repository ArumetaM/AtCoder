import copy

def f0(num):
    if 10>num:
        return "00000"+str(num)
    elif 100>num:
        return "0000"+str(num)
    elif 1000>num:
        return "000"+str(num)
    elif 10000>num:
        return "00"+str(num)
    elif 100000>num:
        return "0"+str(num)
    else:
        return str(num)

N,M = map(int,input().split(" "))
py = []
aaa = []
bbb = []
ccc = []
for i in range(M):
    p,y = map(int,input().split(" "))
    py.append([p,y])
    if p not in aaa:
        aaa.append(p)
        bbb.append([y])
    else:
        bbb[aaa.index(p)].append(y)
for i in range(len(aaa)):
    BBB = copy.deepcopy(bbb[i])
    BBB.sort()
    ccc.append(BBB)
for i in range(M):
    p,y = py[i]
    ans1 = aaa.index(p)
    ans2 = ccc[ans1].index(y)
    print(f0(p)+f0(ans2+1))
