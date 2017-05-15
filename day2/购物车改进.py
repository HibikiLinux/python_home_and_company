#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
shangpin=[("手机",1500),
          ("西瓜",20),
          ("鸡肉",30),
          ("白菜",15),
          ("大米",5),]
gouwuches=[]
gongzi=input("请输入工资：")
if gongzi.isdigit():
    gongzi=int(gongzi)
    while True:
        for ShowShangpin in enumerate(shangpin):
            print(ShowShangpin)
        gouwuche=input("选择要购买的商品:")
        if gouwuche.isdigit():
            gouwuche=int(gouwuche)
            if gouwuche<len(shangpin) and gouwuche>=0:
                jiage=shangpin[gouwuche]
                if jiage[1]<=gongzi:#买得起
                    gouwuches.append(jiage)
                    gongzi=gongzi-jiage[1]
                    print("{0}加入购物车，您的余额为{1}".format(jiage[0],gongzi))
                else:
                    print("余额不足")
            else:
                print("请输入正确的编号")
        elif gouwuche=='q':
            print("退出成功")
            for p in gouwuches:
                print(p)
            print("工资余额为：{0}".format(gongzi))
            break
        else:
            print("请输入正确的编号")




