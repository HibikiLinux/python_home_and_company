#!/usr/bin/env Python
#-*- coding:utf-8 -*-
#Author:yanshen
#著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
#1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

#fib(9)
#这就是定义generator（装饰器）的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
print(fib(9))
for n in fib(9):
    print(n)
g=fib(9)
while True:
    try:
        print("g:",next(g))
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

