#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 16:16
# @Author  : Warren.wang
# @File    : test_rerun_8_1.py
# @Software: PyCharm


'''
命令行：
pytest test_rerun_8_1.py --reruns 5
pytest test_rerun_8_1.py --reruns 5 --reruns-delay 1  #等1s后延迟执行
@pytest.mark.flaky(reruns=5, reruns_delay=2)
'''
import pytest


@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_rerun():
    assert 1 == 2


