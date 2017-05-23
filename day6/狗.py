#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
class Dog:
    def __init__(self,name):
        self.name=name
    def bulk(self):
        print("%s:wang wang wang"%self.name)


d1 = Dog("花花")
d2 = Dog("黑黑")
d3 = Dog("豆豆")

d1.bulk()
d2.bulk()
d3.bulk()
