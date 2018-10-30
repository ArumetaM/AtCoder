N = int(input())
S = input()
east = S.count("E")
west = 0
min = east

for i in S:
    if i == "E":
        east -= 1
    else:
        west += 1
    if min > east + west:
        min = east + west

print(min)
