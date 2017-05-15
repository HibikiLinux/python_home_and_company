#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import sys
f=open("yesterday.txt","r",encoding="utf8")
f_new=open("yesterday_bak.txt","w",encoding="utf8")
find=sys.argv[1]
replace=sys.argv[2]
for line in f:
    if find in line :
        line=line.replace(find,replace)
    f_new.write(line)
f.close()
f_new.close()