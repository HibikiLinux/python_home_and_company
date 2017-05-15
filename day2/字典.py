#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}
print(info)
#增加
#info["stu1104"]="苍井空"
#print(info)
#修改
#info['stu1101'] = "武藤兰"
#print(info)
#删除
#info.pop("stu1101")
#del info
#info.popitem()#随机删除
#print(info)
#查找
a="stu1102" in info
print(a)
#b=info.get("stu1102")
b=info.get("ssss")
print(b)
print(info["stu1101"])
