#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    S = list(map(int,list(input())))
    K = int(input())
    if 1 not in S:
        print(S[0])
        exit()
    else:
        for i in range(K):
            if S[i] != 1:
                print(S[i])
                exit()
        print(1)
