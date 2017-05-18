#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import json
f=open("test.txt","r")
data=json.loads(f.read())
print(data["name"])
f.close()
