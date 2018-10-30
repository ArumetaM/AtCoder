S = input()
flag = 1

while flag > 0:
    flag = 0
    if S[0:11] == "dreameraser":
        S = S[5:]
        flag += 1
    elif S[0:10] == "dreamerase":
        S = S[5:]
        flag += 1
    elif S[0:7] == "dreamer":
        S = S[7:]
        flag += 1
    elif S[0:5] == "dream":
        S = S[5:]
        flag += 1
    if S[0:6] == "eraser":
        S = S[6:]
        flag += 1
    elif S[0:5] == "erase":
        S = S[5:]
        flag += 1

if len(S) == 0:
    print("YES")
else:
    print("NO")
