'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: calenda_api.py
@time: 2021/7/11 17:06
@Email: Warron.Wang
'''
from test_feishu.service.api.feishu_api import FeishuApi


class CalendarApi(FeishuApi):
    '''
    日历管理
    calendar api的统一设置，比如 url前缀，日志的创建、更新、删除和查询
    '''

    def __init__(self):
        super().__init__()
        self.pre_fix = "https://"
        self.host = "open.feishu.cn"
        self.path = "/open-apis/calendar/v4/calendars/"
        self.BASE_URL = f"{self.pre_fix}{self.host}{self.path}"

    def create(self, name):
        """
        创建日历
        :param json: 传入json对象
        :return:
        """
        pass

    def list(self, json):
        """
        获取所有日历
        :param json: 传入json对象
        :return:
        """
        pass

    def get(self, id):
        """
        获取某一条日历
        :param id: 日历id
        :return:
        """
        pass

    def delete(self, id):
        """
        删除某一条日历
        :param id: 日历id
        :return:
        """
        pass

    def update(self, **kwargs):
        """
        更新日历
        :param 多个
        :return:
        """
        pass
