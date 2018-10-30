#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    N,T = map(int,input().split(" "))
    cost = []
    for i in range(N):
        c,t = map(int,input().split(" "))
        if t > T:
            continue
        else:
            cost.append(c)
    if not cost:
        print("TLE")
    else:
        print(min(cost))
