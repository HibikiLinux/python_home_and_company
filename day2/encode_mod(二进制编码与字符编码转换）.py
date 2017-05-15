#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
msg = "我爱北京天安门"
print(type(msg))
print(msg)
msg2=msg.encode(encoding="utf-8")
print(type(msg2))
print(msg2)
msg3=msg2.decode(encoding="utf-8")
print(msg3)