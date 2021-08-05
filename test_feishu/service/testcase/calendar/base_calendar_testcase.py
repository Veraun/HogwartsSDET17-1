'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: base_calendar_testcase.py
@time: 2021/8/5 23:39
@Email: Warron.Wang
'''

from test_feishu.service.api.calendar.calenda_api_http import CalendarApiHttp
from test_feishu.service.testcase.base_feishu_testcase import BaseFeiShuTestCase


class BaseCalendarsTestCase(BaseFeiShuTestCase):
    def setup_class(self):
        self.calendarsApiHttp = CalendarApiHttp()

    def setup(self):
        """
        清理数据
        :return:
        """
        pass

    def teardown(self):
        """
        清理数据，还原环境
        :return:
        """
