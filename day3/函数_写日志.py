#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import time
def logger():
    time_format='%Y-%m-%d %X'
    time_current=time.strftime(time_format)
    with open('a.txt','a+') as f:
        f.write('{0}end action\n'.format(time_current))
def test1():
    print('in the test1')
    logger()
def test2():
    print('in the test2')
    logger()
    return 0
def test3():
    print('in the test3')
    logger()
    return 1,'hello',['alex','wupeiqi']
a=test1()
b=test2()
c=test3()
print(a)
print(b)
print(c)