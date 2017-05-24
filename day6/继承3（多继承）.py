#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
#class People:#经典类的建立方法
class People(object): #新式类建立方法
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print("%s is eating..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

class Relation(object):
    def make_friends(self,obj):
        print("%s is making friend with %s"%(self.name,obj.name))


class men(People,Relation):
    def piao(self):
        print("%s is piaoing ..... 20s....done." % self.name)
    def sleep(self):
        print("man is sleeping ")

class Woman(People,Relation):
    def get_birth(self):
        print("%s is born a baby...." %self.name)

w1=Woman("小红","22")
m1=men("小明","23")
m1.make_friends(w1)