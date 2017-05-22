#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import random
suiji=""
for i in range(4):
    pd=random.randint(0,1)
    if pd==0:
        x=random.randint(0,9)
    else:
        x=chr(random.randint(65,90))
    suiji+=str(x)
print(suiji)