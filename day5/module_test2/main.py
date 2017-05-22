#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import sys,os
print(__file__) #__file__指的是当前文件的绝对路径
print(os.path.abspath(__file__)) #os.path.abspath(path) 返回path规范化的绝对路径。
print(os.path.dirname(os.path.abspath(__file__)))#os.path.dirname(path)返回path的目录。
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
x=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(sys.path)
sys.path.append(x)
print(sys.path)
import module_Alex
print(module_Alex.name)
module_Alex.say_hello()