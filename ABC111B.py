ans = int(input())
if ans%111 == 0:
    print(ans)
else:
    x = int(ans/111+1)
    print(x*111)
