import copy

def ans(list1,list2,list3):
    l1 = copy.deepcopy(list1)
    l2 = copy.deepcopy(list2)
    l3 = copy.deepcopy(list3)
    aa = min(l1)
    bb = l1.index(aa)
    l2[bb] = 1000
    l3[bb] = 1000
    cc = min(l2)
    dd = l2.index(cc)
    l3[dd] = 1000
    ee = min(l3)
    return aa+cc+ee

N,C = map(int,input().split(" "))
D = []
c0 = []
c1 = []
c2 = []

for i in range(C):
    aa = list(map(int,input().split(" ")))
    D.append(aa)
for i in range(N):
    aa = list(map(int,input().split(" ")))
    for j in range(N):
        if (i+j)%3 == 0:
            c0.append(aa[j])
        elif (i+j)%3 == 1:
            c1.append(aa[j])
        else:
            c2.append(aa[j])
c0cost = []
c1cost = []
c2cost = []
for i in range(C):
    cost = 0
    for j in range(len(c0)):
        cost += D[c0[j]-1][i]
    c0cost.append(cost)
for i in range(C):
    cost = 0
    for j in range(len(c1)):
        cost += D[c1[j]-1][i]
    c1cost.append(cost)
for i in range(C):
    cost = 0
    for j in range(len(c2)):
        cost += D[c2[j]-1][i]
    c2cost.append(cost)
print(min(ans(c0cost,c1cost,c2cost),ans(c0cost,c2cost,c1cost),ans(c1cost,c0cost,c2cost),ans(c1cost,c2cost,c0cost),ans(c2cost,c0cost,c1cost),ans(c2cost,c1cost,c0cost)))
