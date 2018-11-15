A,B,C = map(int,input().split(" "))
num1 = max(A,B,C)
num3 = min(A,B,C)
num2 = A+B+C-num1-num3
if (num1*2-num2-num3)%2 == 1:
    print((num1*2-num2-num3)//2+2)
else:
    print((num1*2-num2-num3)//2)
