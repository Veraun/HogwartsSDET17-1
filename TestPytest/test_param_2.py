'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_a_1.py
@time: 2021/5/25 10:13
@Email: Warron.Wang
'''

'''
运行方式：
1 python解释器
2 pytest运行
'''

'''
命令：
pytest --help查看
pytest test_a_1.py -v
pytest -k test_b -v
pytest -k 'test_b or test_a' -v

'''

import pytest


def func(x):
    return x + 1

@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,20),
    ('a','a1'),
    (3,4),
    (5,6)
])
def test_answer(a,b):
    assert func(a) == b


def test_answer1():
    assert func(4) == 5


# 使用fixture
@pytest.fixture()
def login():
    print("登录操作")
    username = 'Jerry'
    return username

class TestDemo:
    # 需要登录
    # 先执行login并返回结果，再执行自己的方法
    def test_a(self, login):
        print(f"login的返回:{login}")
        print("a")

    # 不需要登录
    def test_b(self):
        print("b")

    # 需要登录
    def test_c(self, login):
        print(f"login的返回:{login}")
        print("c")

    def d(self):
        print("d")

if __name__ == '__main__':
    # pytest.main(['test_a_1.py'])
    pytest.main(['test_a_1.py::TestDemo', '-v'])
