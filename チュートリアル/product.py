x = input()
a = int(x.split(" ")[0])
b = int(x.split(" ")[1])
if (a*b)%2 == 0:
    print("Even")
else:
    print("Odd")
