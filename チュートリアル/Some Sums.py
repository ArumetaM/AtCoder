input = input()
N = int(input.split(" ")[0])
A = int(input.split(" ")[1])
B = int(input.split(" ")[2])
count = 0

for i in range(N+1):
    num4 = int(i/10000)
    num3 = int((i-num4*10000)/1000)
    num2 = int((i-num4*10000-num3*1000)/100)
    num1 = int((i-num4*10000-num3*1000-num2*100)/10)
    num0 = int(i-num4*10000-num3*1000-num2*100-num1*10)
    sum = num4 + num3 + num2 + num1 + num0
    if (A <= sum) and (sum <= B):
        count += i


print(count)
