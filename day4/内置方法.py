#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
#abs()#取绝对值
#all()#如果元素都为真返回真
print("all:",all([0,-5,3]))
print("all:",all([-5,3]))
#any()#如果任意一个元素为真返回真
print("any:",any([0,-5,3]))
print("any:",any([]))
#ascii()#把列表变为字符串格式
print(type([1,2,3]),[1,2,3,"啊"])
print(type(ascii([1,2,3,"啊"])),ascii([1,2,3,"啊"]))
#bin()#把数字转成二进制
print(bin(9))
#bytes()改字节格式
a = bytes("abcd",encoding="utf-8")
print(a)
#bytearray()把字符串变列表
b = bytearray("abcd",encoding="utf-8")
print(b[1])
#callable（）看是否可调用
b=[1,2,3]
def sa():pass
print(callable(b))
print(callable(sa))
#chr把数字转化为对应ascll码
print(chr(99))
#ord()把字母转化对应ascll码
print(ord("c"))
#compile()把字符串变成可执行代码
#exec（）执行字符串
#eval()执行字符串（不能有语句）
a="print(1+1)"
exec(a)
#dict()生成字典
#dir()查看方法
print(dir(a))
#divmod(a,b)a除以b返回余数
print(divmod(9,2))
#enumerate#将可循环序列sequence以start开始分别列出序列数据和数据下标
a=["a","b","c,","d"]
for i in enumerate(a,1):
    print(i)
#匿名函数
calc =lambda n:n*n
print(calc(3))
#filter()过滤
res=filter(lambda n:n>5,range(10))
for i in res:
    print(i)
#map()运算
res = map(lambda n:n*2,range(10))
for i in res:
    print(i)
#reduce累计运算
import functools
res =functools.reduce(lambda x,y:x+y,range(4))
print(res)
#frozenset() 使列表不可变
#globals()程序内的所有变以字典格式
print(globals())
#hex转16进制
#oct（）8进制
#sorted()使字典列表有序有序
a={1:2,3:6,6:4}
b=(3,2,4,5,6,)
print(sorted(a.items()))
print(sorted(a.items(),key=lambda x:x[1]))
print(sorted(b))
#zip（）拼接拉链
a=[1,2,3,4,5]
b=['a','b','c']
for i in zip(a,b):
    print(i)
#_import_()引用模块可以用字符串
#import ceshi
__import__("ceshi")
