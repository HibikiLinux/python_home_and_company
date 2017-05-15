#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import os
cmd_res = os.popen("dir").read()
print(cmd_res)
os.mkdir("new_dir")