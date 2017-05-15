#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
#t =set("sss")
#s =set([3,5,6,7])
#print(s)
#a= t | s
#print(a)
#b= t&s
#c=t-s
#d=t^s
#t.add('x')
#print(t)
#print(len(t))
a=set([1,2,3,4,5,6,7])
b=set([1,2,3])
c=b.issubset(a)
d=a.issuperset(b)
print(c)
print(d)
d=a.union(b)
print(d)
d=a.intersection(b)
print(d)
d=a.difference(b)
print(d)
d=a.symmetric_difference(b)
print(d)
