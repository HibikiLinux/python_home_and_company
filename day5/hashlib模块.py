#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
import hashlib
#用于加密相关的操作#主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法，
m=hashlib.md5()
m.update(b"12345678")
print(m.digest())#二进制哈希
print(m.hexdigest())#16进制哈希
print(len(m.hexdigest()))
n=hashlib.md5()
n.update(b"1234")
n.update(b"5678")
print(n.digest())
print(n.hexdigest())