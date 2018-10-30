import collections

def answer(list,n):
    Even = collections.Counter(list[::2]).most_common(2)
    Odd = collections.Counter(list[1::2]).most_common(2)

    if Even[0][0] != Odd[0][0]:
        return n - Even[0][1] - Odd[0][1]
    else:
        if len(Even) == 1 or len(Odd) == 1:
            return n // 2
        else:
            return n - max(Even[0][1]+Odd[1][1],Even[1][1]+Odd[0][1])

N = int(input())
list = input().split(" ")
print(answer(list,N))
