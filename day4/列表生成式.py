#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
b=[]
for i in range(10):
    b.append(i*2)
print(b)
a=[i*2 for i in range(10)]#列表生成式
print(a)
c=(i*2 for i in range(10))#生成器
print(c)
for n in c:
    print(n)
