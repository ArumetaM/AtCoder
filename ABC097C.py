s = input()
K = int(input())
dict = []

for i in range(len(s)):
    for k in range(6):
        if s[i:min(i+k,len(s))] not in dict:
            dict.append(s[i:min(i+k,len(s))])
dict.sort()
print(dict[K])
