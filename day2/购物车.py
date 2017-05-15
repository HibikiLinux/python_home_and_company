#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
shouji=["1","手机","1500"]
xigua=["2","西瓜","20"]
jirou=["3","鸡肉","30"]
baicai=["4","白菜","15"]
dami=["5","大米","5"]
gongzi=input("请输入工资：")
gongzi=int(gongzi)
yue=gongzi
zongji=0
gouwuche=[]
while True:
    print(shouji)
    print(xigua)
    print(jirou)
    print(baicai)
    print(dami)
    print("已经购买商品:",gouwuche)
    print("剩余工资:", yue)
    goumai=input("请输入商品序号（退出是q）：")
    if goumai=="1":
        if yue<1500:
            print("你没钱请重选")
            continue
        else:
            zongji=zongji+1500
            gouwuche.append("手机")
    elif goumai=="2":
        if yue<20:
            print("你没钱请重选")
            continue
        else:
            zongji=zongji+20
            gouwuche.append("西瓜")
    elif goumai=="3":
        if yue<30:
            print("你没钱请重选")
            continue
        else:
            zongji=zongji+30
            gouwuche.append("鸡肉")
    elif goumai=="4":
        if yue<15:
            print("你没钱请重选")
            continue
        else:
            zongji=zongji+15
            gouwuche.append("白菜")
    elif goumai=="5":
        if yue<5:
            print("你没钱请重选")
            continue
        else:
            zongji=zongji+5
            gouwuche.append("大米")
    elif goumai=="q":
        break
    else:
        print("输入有误")
    gouwuche.sort()
    yue=gongzi-zongji

print("剩余工资:",yue)
print("商品总价:",zongji)
print(gouwuche)