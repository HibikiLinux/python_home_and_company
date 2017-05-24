#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
#class People:#经典类的建立方法
class Peopel(object): #新式类建立方法
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
    #继承后重构父类
    def __init__(self,name,age,money):
        #两种方式一样
        #People.__init__(self,name,age)#经典类的写法
        super(men,self).__init__(name,age)#新式类的写法

        self.money=money
    def piao(self):
        print("%s is piaoing ..... 20s....done." % self.name)

    def sleep(self):
        print("man is sleeping ")

m1=People('小明','22')
m2=men('小明','22',10)
m1.sleep()
m2.sleep()