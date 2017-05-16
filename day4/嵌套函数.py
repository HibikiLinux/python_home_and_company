#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
def foo():
    print("in the foo")
    def bar():
        print("in the bar")
    bar()
foo()