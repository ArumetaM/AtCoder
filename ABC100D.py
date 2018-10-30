N,M = map(int,input().split(" "))
sum1 = []
sum2 = []
sum3 = []
sum4 = []
sum5 = []
sum6 = []
sum7 = []
sum8 = []

for i in range(N):
    x,y,z = map(int,input().split(" "))
    a1 = x+y+z
    sum1.append(a1)
    #+++
    a2 = a1-z*2
    sum2.append(a2)
    #++-
    a3 = a2-y*2
    sum3.append(a3)
    #+--
    a4 = a3+z*2
    sum4.append(a4)
    #+-+
    a5 = a4-x*2
    sum5.append(a5)
    #--+
    a6 = a5+y*2
    sum6.append(a6)
    #-++
    a7 = a6-z*2
    sum7.append(a7)
    #-+-
    a8 = a7-y*2
    sum8.append(a8)
    #---
sum1.sort()
sum1.reverse()
sum2.sort()
sum2.reverse()
sum3.sort()
sum3.reverse()
sum4.sort()
sum4.reverse()
sum5.sort()
sum5.reverse()
sum6.sort()
sum6.reverse()
sum7.sort()
sum7.reverse()
sum8.sort()
sum8.reverse()
print(max(sum(sum1[:M]),sum(sum2[:M]),sum(sum3[:M]),sum(sum4[:M]),sum(sum5[:M]),sum(sum6[:M]),sum(sum7[:M]),sum(sum8[:M])))
