'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_contact.py
@time: 2021/3/12 09:09
@Email: Warron.Wang
'''

# 装饰器使用

def b(func): #func == a
    def run(*args, **kwargs):  # args == ("我是k")
        print("你好")
        func(*args, **kwargs)  # 装饰器：调用a("我是k")
        print("再见")
    return run

@b
def a(k):       # 被装饰对象
    print("我是a")
    print(k)

def test():     # 调用
    a("我是k")