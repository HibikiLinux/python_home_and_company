#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
av_catalog = {
    "欧美":{
        "aaa": ["44444","22222"],
        "bbb": ["4444","44444444"],
        "ccc": ["111,22","333"],
        "ddd":["123","456"]
    },
    "日韩":{
        "sssss":["ssss1","wewewe"]
    },
    "大陆":{
        "1024":["ccccc","zzzzz"]
    }
}

av_catalog["大陆"]["1024"][1] = ",可以用爬虫爬下来"
print(av_catalog["大陆"]["1024"])
#ouput
['全部免费,真好,好人一生平安', '服务器在国外,慢,可以用爬虫爬下来']