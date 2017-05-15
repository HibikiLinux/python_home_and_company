#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
def calc(n):
    print(n)
    if int(n/2)>0:
        return calc(int(n/2))
    print("----")
calc(10)