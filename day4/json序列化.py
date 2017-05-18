#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import json
info={"name":"alex","age":22}
f=open("test.txt","w")
f.write(json.dumps(info))
f.close()