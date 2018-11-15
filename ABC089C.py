N = int(input())
countM = 0
countA = 0
countR = 0
countC = 0
countH = 0
for i in range(N):
    s = input()
    if (s[0] == "M"):
        countM += 1
        continue
    elif (s[0] == "A"):
        countA += 1
        continue
    elif (s[0] == "R"):
        countR += 1
        continue
    elif (s[0] == "C"):
        countC += 1
        continue
    elif (s[0] == "H"):
        countH += 1
print(countM*countA*countR+countM*countA*countC+countM*countA*countH+countM*countR*countC+countM*countR*countH+countM*countC*countH+countA*countR*countC+countA*countR*countH+countA*countC*countH+countR*countC*countH)
