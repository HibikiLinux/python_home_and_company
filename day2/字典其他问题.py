#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}
#print(info)
#a=(info.values())
#print(a)
#print(info)
#a=info.keys()
#print(a)
#没有新建，有不动
#a=info.setdefault("stu1106","alex")
#print(a)
#print(info)
#a=info.setdefault("stu1102","bbb")
#print(a)
#print(info)
#更新
#b = {1:2,3:4, "stu1102":"龙泽萝拉"}
#info.update(b)
#print(info)
#拆解成元组
#print(info.items())
for key in info:
    print(key,info[key])
print("--------")
for a in info:
    print(a,info[a])
    print(a)
