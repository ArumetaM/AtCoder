def answer(aaa,max):
    half = max / 2
    bbb = []
    for i in range(len(aaa)):
        bbb.append(abs(half - aaa[i]))
    return aaa[bbb.index(min(bbb))]


n = int(input())
a = list(map(int,input().split(" ")))
b = max(a)
a.remove(b)
print(b,answer(a,b))
