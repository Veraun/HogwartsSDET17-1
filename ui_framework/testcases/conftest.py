'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: conftest.py
@time: 2021/3/16 08:29
@Email: Warron.Wang
'''
import os
import signal
import subprocess

import pytest

# 录屏:scrcpy
@pytest.fixture(scope="module", autouse=True)
def record():
    # 用例运行前做一些事情
    cmd = "scrcpy -p 1234 -m 800 -Nr tmp.mp4"
    p = subprocess.Popen(cmd, shell=True)
    yield
    # 用例运行后做一些事情
    os.kill(p.pid, signal.SIGINT)