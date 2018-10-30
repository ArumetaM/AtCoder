#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    N = int(input())
    inf = []
    a = []
    for i in range(N):
        x,y,h = map(int,input().split(" "))
        inf.append([x,y,h])
        if h >= 1:
            a.append([x,y,h])
    X = a[0][0]
    Y = a[0][1]
    H = a[0][2]
    center = []
    for i in range(101):
        for j in range(101):
            h = H + abs(X-i) + abs(Y-i)
            center.append([i,j,h])
    for i in range(len(inf)):
        x = inf[i][0]
        y = inf[i][1]
        h = inf[i][2]
        list = []
        for j in range(len(center)):
            if h == center[j][2] - abs(x-center[j][0]) - abs(y-center[j][1]):
                list.append(center[j])
        center = list
        if len(center) == 1:
            print(center[0][0],center[0][1],center[0][2])
            exit()
