#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

if __name__ == "__main__":
    list = input().split(" ")
    N = int(list[0])
    M = int(list[1])
    list = []
    for i in range(1,int(math.sqrt(M)+1)):
        if M%i == 0:
            list.append(i)
    for i in range(len(list)):
        list.append(int(M/list[i]))
    list.reverse()
    for i in range(len(list)):
        if M/list[i] >= N:
            print(list[i])
            exit()
