#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import time
def timer(func):  #timer(test1)----》func=test1
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)  #执行了test1
        stop_time=time.time()
        print("the func run timo is {0}".format(stop_time-start_time))
    return deco
@timer #相当于在下面执行了test1=timer(test1)
def test1():
    time.sleep(1)
    print("in the test1")
@timer
def test2(name,age):
    time.sleep(1)
    print("in the test2,{0},{1}".format(name,age))
#test1=timer(test1)
test1() #实际上是在执行deco
est2("alex",22)