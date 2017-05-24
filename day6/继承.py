#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print("%s is eating..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

class men(People):
    def piao(self):
        print("%s is piaoing ..... 20s....done." % self.name)

    def sleep(self):
        print("man is sleeping ")

m1=People('小明','22')
m2=men('小明','22')
m1.sleep()
m2.sleep()