'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_calendar.py
@time: 2021/7/11 17:13
@Email: Warron.Wang
'''
import pytest

from test_feishu.service.tests.calendar.BaseCalendarTestCase import BaseCalendarTestCase


class TestCalendar(BaseCalendarTestCase):
    def setup(self):
        pass

    def teardown(self):
        pass

    # 参数化+数据驱动
    # 纯数据驱动，把测试用例步骤也数据化：类似httprunner
    @pytest.mark.parametrize()
    def test_create(self):
        self.calendar.create()
        self.calendar.list()
        # todo
