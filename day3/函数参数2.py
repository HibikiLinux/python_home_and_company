#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
#默认参数
def test(x,y=5):
    print(x)
    print(y)
test(x=1)
test(2,6)
#参数组
#以*开头，arges是变量 *agrge接受N个位置参数，转换成元组
def test2(*args):
    print(args)
test2(1,2,3,4,5)
test2(*[1,2,3,4,5,6])
#把n个参数作为字典 **kwargs接收的是N个关键字参数，转换成字典
def test3(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['sex'])

test3(name='alex',age=8,sex='f')
test3(**{'name': 'alex','age': 8,'sex': 'f'})

