#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
#列表字典可以在局部更改全局
name=["Alex","Jack","Rain"]
def chage_name():
    name[0]="金角大王"
    print(name)
chage_name()
print(name)