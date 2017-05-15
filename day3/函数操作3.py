#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
def test(name,age=18,**kwargs):
    print(name)
    print(kwargs)
    print(age)
test('alex',age=18,sex='m')