#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import time
class Role(object):
    n="战士"
    name="士兵" #类变量
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        #构造函数，
        #属性=变量
        #在实例化时做一些类的初始化工作
        self.name = name #实例变量（静态属性） #作用域实例本身
        self.role = role
        self.weapon = weapon
        #私有属性，直接加“__",私有属性只能内部访问，在class里面
        self.__life_value = life_value
        self.money = money

    def shot(self):#类方法（动态属性）
        print("shooting...")
        #私有方法也一样加“__”
    def got_shot(self):
        self.__life_value -= 1
        print("ah...,%s got shot..."%self.name)

    def buy_gun(self,gun_name):
        print("just bought %s"%gun_name)

    def show_status(self):
        print("{0} have {1}".format(self.name,self.__life_value,))

#析构函数：在实例释放、摧毁的时候自动执行，通常用于做一些收尾工作
#关闭一些数据库连接，打开临时文件
   # def __del__(self):
   #     print("%s 彻底死了"%self.name)


r1 = Role('Alex', 'police', 'AK47')#实例化，造了一个对象
r2 = Role('Jack', 'terrorist', 'B22')
# r1.shot()# ===>Role.shot(r1)
# r1.got_shot()
# print(r1.name)
# r1.buy_gun("M4")
# print(Role.name)
# print(Role.n)
# print(r1.n)
######改变对象属性##########
# r1.name="王小明" #改变对象属性
# r1.bullet_prove=True #增加对象的属相
# del  r1.weapon #删除属性，卸掉武器
# print(r1.name,r1.bullet_prove)
# print(r1.n)
# print(r2.n)
# r1.n="666"
# print("----")
# print(r1.n)
# print(r2.n)
r1.show_status()
r1.got_shot()
r1.show_status()