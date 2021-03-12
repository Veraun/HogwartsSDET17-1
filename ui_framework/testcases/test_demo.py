'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_demo.py
@time: 2021/3/12 09:09
@Email: Warron.Wang
'''

# 装饰器使用

def b(func):
    def run(*args, **kwargs):
        print("你好")
        func(*args, **kwargs)
        print("再见")
    return run

@b
def a(k):
    print("我是a")
    print(k)

def test():
    a("我是k")