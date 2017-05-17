#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
def auth(auth_type):
    print("auth func:",auth_type)
    def outer_wrapper(func()):
        def wrapper(*args,**kwargs):
            user=input("user:")
            passwd=input("passsword:")
            if user=="yan" and passwd=="666666":
                func()
            else:
                exit("your user or password is error.")
        return wrapper
    return outer_wrapper
@auth(auth_type="local")
def index():
    print("welcome index!!")
@auth(auth_type=" local")
def home():
    print("welcom home!!")
@auth(auth_type"ladap")
def bbs():
    print("welcome bbs!!")
home()
