#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen

def te(x,y):
    print(x)
    print(y)
#位置参数调用
te(1,2)
#关键字调用
te(y=3,x=4)
#
#关键参数要写在位置参数后面
te(6,y=6)