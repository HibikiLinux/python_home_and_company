#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import time
#时间戳转化为struct_time
x=time.localtime()
x1=time.localtime(0)
print(x)
print(x.tm_year)
print(x1)
#struct_time转化为时间戳
l=time.mktime(time.localtime())
l1=time.mktime(time.localtime(0))
print(l)
print(l1)
#struct_time转化为时间字符串
print(time.strftime("%Y-%m-%d %H:%M:%S",x))
print(time.strftime("%Y-%m-%d %H:%M:%S",x1))
#时间字符串转化为struct_time
print(time.strptime('2017-05-22 14:12:53',"%Y-%m-%d %H:%M:%S"))
#简化struct_time
print(time.asctime())
#简化时间戳
print(time.ctime(666))
