#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import time
def add(x,y,f):
    return f(x) + f(y)
def ab(n):
    return n*n
res = add(3,-6,ab)
print(res)

def bar():
    time.sleep(1)
    print("in the bar")
def test2(func):
    print("sss",func)
    return func
bar()
t=test2(bar)
t()
