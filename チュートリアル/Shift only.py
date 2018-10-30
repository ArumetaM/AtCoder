def EvenJudge(list,N):
    a = 0
    for i in range(N):
        if list[i]%2 == 1:
            a += 1
    if a > 0:
        return 1
    else:
        return 0

N = int(input())
x = input()
BB = []
count = 0
for i in range(N):
    BB.append(int(x.split(" ")[i]))

while EvenJudge(BB,N) == 0:
    for i in range(N):
        BB[i] = BB[i] / 2
    count += 1
print(count)
