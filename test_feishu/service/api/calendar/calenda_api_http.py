'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: calenda_api.py
@time: 2021/7/11 17:06
@Email: Warron.Wang
'''
from test_feishu.service.api.calendar.calenda_api import CalendarApi


class CalendarApiHttp(CalendarApi):
    '''
    实现业务行为的具体操作
    '''

    def create(self, json):
        '''
        创建日历
        :param json:传入json对象
        :return:
        '''
        res = self.send_request('POST', self.BASE_URL, json=json)
        return res.json()

    def list(self, json: object = {'page_size': 500}):
        """
        获取所有日历
        :param json: 传入json对象
        :return:
        """
        res = self.send_request('get', self.BASE_URL, json=json)
        return res.json()

    def get(self, id):
        calendar_id = f"feishu.cn_{id}@group.calendar.feishu.cn"
        url = f"{self.BASE_URL}/{calendar_id}"
        res = self.send_request('get', url)
        return res.json()

    def delete(self, id):
        url = f"{self.BASE_URL}/{id}"
        res = self.send_request('delete', url)
        return res.json()

    def update(self, data):
        id = data["id"]
        url = f"{self.BASE_URL}/{id}"
        json = {}
        for key in data.keys():
            json[key] = data[key]
        res = self.send_request('patch', url, json=json)
        return res.json()