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
链式栈
'''
import pytest


class StackBaseOnLinkedList:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = self.Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            return -1
        result = self.top.data
        self.top = self.top.next
        return result


    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None



def test_static():
    stack = StackBaseOnLinkedList()
    data = [1, 2, 3, 4, 5]
    for i in data:
        stack.push(i)
    data.reverse()

    for i in data:
        assert i == stack.pop()
    assert stack.pop() == -1

if __name__ == '__main__':
    pytest.main(["-v", "-s"])
