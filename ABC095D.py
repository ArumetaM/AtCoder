N,C = map(int,input().split(" "))
table = []
for i in range(N):
    aa = input().split(" ")
    x = int(aa[0])
    v = int(aa[1])
    table.append([x,v])
table.sort()
Status = table[0][1] - table[0][0]
Mstatus = table[0][1] - table[0][0]
place = table[0][0]
table.remove([table[0][0],table[0][1]])

for i in range(N-1):
    right = (table[0][1] - abs(table[0][0]-place))
    left = (table[N-i-2][1] - abs(table[N-i-2][0] - place))
    if right >= left:
        place = table[0][0]
        table.remove([table[0][0],table[0][1]])
    else:
        place = table[N-i-2][0]
        table.remove([table[N-i-2][0],table[N-i-2][1]])
    Status += max(right,left)
    if Status > Mstatus:
        Mstatus = Status

print(Mstatus)
