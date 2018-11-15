grid = []
all = 0
for i in range(3):
    c1,c2,c3 = map(int,input().split(" "))
    all += c1
    all += c2
    all += c3
    grid.append([c1,c2,c3])
if (all//3 > 600)or(all < 0):
    print("No")
    exit()
else:
    for i in range(101):
        a1=i
        b1 = grid[0][0] - a1
        b2 = grid[0][1] - a1
        b3 = grid[0][2] - a1
        a2 = grid[1][0] - b1
        a3 = grid[2][0] - b1
        if (a2+b2==grid[1][1])and(a2+b3==grid[1][2])and(a3+b2==grid[2][1])and(a3+b3==grid[2][2]):
            print("Yes")
            exit()
print("No")
