'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: tmp_lianshi_queue.py
@time: 2021/5/20 17:51
@Email: Warron.Wang
'''
import pytest


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # 入队 从尾入
    def enqueue(self, item):
        if self.tail is None:
            new_node = self.Node(item)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = self.Node(item)
            self.tail = self.tail.next

    # 出队 从头出
    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.data
        self.head = self.head.next
        return value


    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


def test_queue():
    a =Queue()
    a.enqueue("10")
    a.enqueue("20")
    a.enqueue("30")
    deque_item = a.dequeue()
    assert deque_item == "10"
    assert a.head.data == "20"
    assert a.head.next.data == "30"

if __name__ == '__main__':
    pytest.main(["-v", "-s"])