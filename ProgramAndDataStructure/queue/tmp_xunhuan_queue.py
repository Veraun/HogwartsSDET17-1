'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: tmp_xunhuan_queue.py
@time: 2021/5/20 18:26
@Email: Warron.Wang
'''

import pytest


class Queue:
    def __init__(self, capacity) -> None:
        self.n = capacity
        self.items = [-1] * capacity
        self.header = 0
        self.tail = 0

    # 入队 从尾进
    def enqueue(self, item):
        if (self.tail + 1) % self.n == self.header:
            return False
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.n
        return True

    # 出队 从头出
    def dequeue(self):
        if self.header == self.tail:
            return None
        value = self.items[self.header]
        self.header = (self.header + 1) % self.n
        return value

def test_queue():
    a = Queue(10)
    a.enqueue("10")
    a.enqueue("20")
    deque_item = a.dequeue()
    assert deque_item == "10"

    a.enqueue("30")
    assert a.items[a.header] == "20"
    assert a.items[a.tail - 1] == "30"

if __name__ == '__main__':
    pytest.main(["-v", "-s"])


