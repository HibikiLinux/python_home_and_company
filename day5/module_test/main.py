#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import module_Alex #本质上就是把module_Alex所有代码赋值给了module_Alex
def say_hello():
    print('你好')
print(module_Alex.name)
module_Alex.say_hello()
