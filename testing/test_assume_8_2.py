#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 19:38
# @Author  : Warren.wang
# @File    : test_assume_8_2.py
# @Software: PyCharm

'''
多条断言，互不影响
前面失败，后面会继续执行
'''
import pytest


# def test_assume():
#     # assert 1 == 1
#     # assert 1 == 2
#     # assert 2 == 3
#     pytest.assume(1 == 1)
#     pytest.assume(1 == 2)
#     pytest.assume(2 == 3)
#     pytest.assume(4 == 4)
#     pytest.assume


class Test(object):

    def test_01(self):
        """用例1"""
        print('执行test_01断言1')
        pytest.assume(0 == 1)
        print('执行test_01断言2')
        pytest.assume(1 == 2)

    def test_02(self):
        """用例2"""
        print('执行test_02断言1')
        pytest.assume(3 == 5)
        print('执行test_02断言2')
        pytest.assume(4 == 4)


if __name__ == '__main__':
    pytest.main(['-s', 'test_assume_8_2.py'])

