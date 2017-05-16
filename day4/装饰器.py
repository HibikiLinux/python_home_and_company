#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import time
def timmer(func):
    start_time=time.time()
    func()
    stop_time=time.time()
    print("then func run time is %s"%(stop_time-start_time))
def bar():
    time.sleep(1)
    print("hello world")
timmer(bar)