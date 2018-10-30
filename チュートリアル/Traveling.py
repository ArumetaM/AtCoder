N = int(input())
travel = [0,0]
time = 0

for i in range(N):
    list = input()
    t = int(list.split(" ")[0])
    x = int(list.split(" ")[1])
    y = int(list.split(" ")[2])
    t -= time

    if (abs(travel[0] - x) + abs(travel[1] - y) > t)or((abs(travel[0] - x) + abs(travel[1] - y) - t)%2 == 1):
        print("No")
        exit()
    else:
        time += t
        travel[0] = x
        travel[1] = y

print("Yes")
