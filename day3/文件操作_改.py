#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
f=open("yesterday.txt","r",encoding="utf8")
f_new=open("yesterday_bak.txt","w",encoding="utf8")

for line in f:
    if "有那么多肆意的快乐等我享受" in line :
        line=line.replace("有那么多肆意的快乐等我享受","alex")
    f_new.write(line)
f.close()
f_new.close()
