#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
def auth(func):
    def wrapper():
        user=input("user:")
        passwd=input("passsword:")
        if user=="yan" and passwd=="666666":
            #func()
            return func()
        else:
            exit("your user or password is error.")
    return wrapper
@auth
def index():
    print("welcome index!!")
@auth
def home():
    print("welcom home!!")
    return "home"
@auth
def bbs():
    print("welcome bbs!!")
print(home())