S = list(input())
T = list(input())

for i in range(len(S)):
    if (T[i] == S[i])or(T[i] == 0):
        continue
    else:
        for j in range(T.count(T[i])):
            x = T.index(T[i])
            if S[x] == S[i]:
                T[x] = 0
                continue
            else:
                print("No")
                exit()

print("Yes")
