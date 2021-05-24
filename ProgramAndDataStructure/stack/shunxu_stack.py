'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: shunxu_stack.py
@time: 2021/5/20 19:55
@Email: Warron.Wang
'''

'''
顺序栈
'''
import pytest


class ArrayStack:
    def __init__(self, n):
        self.data = [-1] * n
        self.n = n  # 栈容量
        self.count = 0  # 当前有多少个数据

    # 入栈
    def push(self, value):
        if self.n == self.count:
            return False
        self.data[self.count] = value
        self.count += 1
        return True

    # 出栈
    def pop(self):
        if self.count == 0:
            return None
        self.count -= 1
        return self.data[self.count]

def test_static():
    array_stack = ArrayStack(5)
    data = ["a", "b", "c", "d", "e"]
    for i in data:
        array_stack.push(i)
    result = array_stack.push("a")
    assert not result

    data.reverse()
    # print(data)
    # print(array_stack.pop())
    for i in data:
        assert i == array_stack.pop()
    assert array_stack.pop() is None

if __name__ == '__main__':
    pytest.main(["-v", "-s"])
