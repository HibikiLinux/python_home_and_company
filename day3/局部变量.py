#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
def change_name(name):
    global school
    school="mage"
    print(school)
    print("before chage",name)
    name="Alex li"#这个函数就是这个变量的作用域
    age=23
    print("after change",name)
school="oldboy"
name="alex"
change_name(name)
print(name)
print(school)