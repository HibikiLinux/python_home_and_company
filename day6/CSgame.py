#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
class Role(object):
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("just bought %s" % gun_name)

r1 = Role('Alex', 'police', 'AK47')#实例化，造了一个对象
r2 = Role('Jack', 'terrorist', 'B22')
