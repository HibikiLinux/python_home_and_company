#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen

def test(x,y):
    print(x)
    print(y)
#位置参数调用
test(1,2)
#关键字调用
test(y=3,x=4)
#
#关键参数要写在位置参数后面
test(6,y=6)