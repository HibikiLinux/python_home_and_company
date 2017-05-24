#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import time
def timer(func):  #timer(test1)----》func=test1
    def dd():
        start_time=time.time()
        func()  #执行了test1
        stop_time=time.time()
        print("the func run timo is {0}".format(stop_time-start_time))
    return dd

def test1():
    time.sleep(1)
    print("in the test1")

def test2():
    time.sleep(1)
    print("in the test2")

test1=timer(test1)
test1()
 #实际上是在执行deco
