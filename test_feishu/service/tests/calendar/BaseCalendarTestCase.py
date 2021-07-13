'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: BaseCalendarTestCase.py
@time: 2021/7/12 15:34
@Email: Warron.Wang
'''
from test_feishu.service.api.calendar.calenda_api import CalendarApi
from test_feishu.service.tests.base_feishu_testcase import BaseFeiShuTestCase


class BaseCalendarTestCase(BaseFeiShuTestCase):
    def setup_class(self):
        # super().setup_class()
        token_data = "../data/token_data.yaml"
        url_path = "../data/url_data.yaml"
        calendar_data = "../data/calendar_data.yaml"

        # 获取token需要的id和secret
        self.app_id = get_data(token_data)["app_id"]
        self.app_secret = get_data(token_data)["app_secret"]

        # 获取token的url
        self.token_url = get_data(url_path)["token_url"]

        # 创建日历的url
        self.create_url = get_data(url_path)["create_calendar_url"]

        # 获取日历的url
        self.get_url = get_data(url_path)["get_calendar_url"]

        # 创建日历列表的url
        self.list_url = get_data(url_path)["calendar_list_url"]

        self.calendar = CalendarApi()