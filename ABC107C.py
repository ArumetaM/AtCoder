#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    N,K = map(int,input().split(" "))
    place = list(map(int,input().split(" ")))
    time = []
    for i in range(N-K+1):
        left = place[i]
        right = place[i+K-1]
        n1 = abs(left) + abs(right - left)
        n2 = abs(right) + abs(left - right)
        time.append(min(n1,n2))
    print(min(time))
