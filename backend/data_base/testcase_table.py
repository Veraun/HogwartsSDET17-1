'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: business-test-pytest
@file: testcase_table.py
@time: 2021/6/7 15:53
@Email: Warron.Wang
'''

# 使用db，可以让类映射到数据库中的User表
from backend.backend_server import db


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键，唯一标识，类似身份证
    nodeid = db.Column(db.String(80), unique=True, nullable=False)  # 唯一；必填项
    description = db.Column(db.String(120), unique=False, nullable=True)

    def as_dict(self):
        '''
        返回测试用例的数据
        :return:
        '''
        return {'id': self.id, "nodeid": self.nodeid, "description": self.description}
