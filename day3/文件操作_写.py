#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
f = open("yesterday2.txt",'w',encoding="utf-8")
f.write("我爱北京天安门\n")
f.write("北京天安门太阳升\n")
f.close()
f = open("yesterday2.txt",'a',encoding="utf-8")
f.write("when i was young\n")
f.close()
f =f = open("yesterday2.txt",'w+',encoding="utf-8")
print(f.readline())
f.write("I love you")
print(f.tell())
f.seek(0)
print(f.read())