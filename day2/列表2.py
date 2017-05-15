#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import copy
name=["hibiki","yamato",["yibuki","fubuki"],"yamato"]
#name2=name #一层也不拷贝
#name2=name.copy() #浅拷贝
#name2=copy.copy(name) #浅拷贝
name2=name[:]
name3=copy.deepcopy(name)#深拷贝
name[1]="xxxx"
name[2][1]="cccc"
print(name)
print(name2)
print(name3)