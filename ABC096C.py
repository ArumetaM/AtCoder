H,W = map(int,input().split(" "))
picture = []

for i in range(H):
    picture.append(list(input()))

for i in range(H):
    for j in range(W):
        if picture[i][j] == "#":
            if i == 0:
                if (j == 0)and(picture[0][1] == ".")and(picture[1][0]):
                    print("No")
                    exit()
                elif (j == W-1)and(picture[0][j-1] == ".")and(picture[1][j] == "."):
                    print("No")
                    exit()
                else:
                    if (picture[i][j-1] == ".")and(picture[i+1][j] == ".")and(picture[i][j+1] == "."):
                        print("No")
                        exit()
            elif i == H-1:
                if (j == 0)and(picture[i-1][j] == ".")and(picture[i][j+1] == "."):
                    print("No")
                    exit()
                elif (j == W-1)and(picture[i-1][j] == ".")and(picture[i][j-1] == "."):
                    print("No")
                    exit()
                else:
                    if (picture[i][j-1] == ".")and(picture[i-1][j] == ".")and(picture[i][j+1] == "."):
                        print("No")
                        exit()
            elif j == 0:
                if (picture[i+1][j] == ".")and(picture[i][j+1] == ".")and(picture[i-1][j] == "."):
                    print("No")
                    exit()
            elif j == W-1:
                if (picture[i-1][j] == ".")and(picture[i][j-1] == ".")and(picture[i+1][j] == "."):
                    print("No")
                    exit()
            else:
                if (picture[i+1][j] == ".")and(picture[i-1][j] == ".")and(picture[i][j+1] == ".")and(picture[i][j-1] == "."):
                    print("No")
                    exit()
print("Yes")
