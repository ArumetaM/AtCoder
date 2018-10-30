#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    N,M,Q = map(int,input().split(" "))
    LR = []
    for i in range(M):
        L,R = map(int,input().split(" "))
        LR.append([L,R])
    for i in range(Q):
        l,r = map(int,input().split(" "))
        count = 0
        for i in range(M):
            if (l <= LR[i][0])and(R = LR[i][1] <= r):
                count += 1
        print(count)
