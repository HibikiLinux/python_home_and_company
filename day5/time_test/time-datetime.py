#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import datetime
#当前时间
print(datetime.datetime.now())
#时间加减
print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分
