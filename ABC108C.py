a = input()
N = int(a.split(" ")[0])
K = int(a.split(" ")[1])
count = 0
if K%2 == 1:
    count = int(N/K)**3
else:
    count = int(N/K)*int(N/K)*int(N/K)*2
    if int(N/K)*K + K/2 <= N:
        count = int(count/2) + (int(N/K)+1)**3
print(count)
