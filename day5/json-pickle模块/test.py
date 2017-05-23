#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
# 用于序列化的两个模块
# json，用于字符串 和 python数据类型间进行转换
# pickle，用于python特有的类型 和 python的数据类型间进行转换
import pickle
data = {'k1':123,'k2':'hello'}
print(data)
p=pickle.dumps(data)
print(p)
with open('1.pk','w') as fp:
    pickle.dump(data,fp)