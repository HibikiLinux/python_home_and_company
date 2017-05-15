#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
f = open("yesterday.txt",'r',encoding="utf-8")
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(1)
print(f.tell())
print(f.readline())
print(f.tell())
