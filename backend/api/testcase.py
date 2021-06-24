'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: business-test-pytest
@file: testcase.py
@time: 2021/6/7 15:52
@Email: Warron.Wang
'''

# 定义测试用例接口
import jenkins
from flask import request
from flask_restful import Resource

from backend.api.verify_token import auth
from backend.backend_server import db
from backend.data_base.testcase_table import TestCase


class TestCaseAdd(Resource):
    method_decorators = [auth.login_required]
    def post(self):
        '''
        新增测试用例
        :return:
        '''
        # 可以利用 request.json获取post传过来的请求体
        nodeid = request.json.get("nodeid")
        description = request.json.get("description")
        # 把请求体中的数据，发送到数据库
        data = TestCase(**request.json)
        db.session.add(data)
        db.session.commit()
        return {"msg": "OK"}


class TestCaseDelete(Resource):
    method_decorators = [auth.login_required]
    # get 方法代表接收get请求
    def get(self):
        '''
        删除测试用例
        :return:
        '''
        # http://127.0.0.1:5000/testcase/delete?nodeid=nodeid_w1
        # 如果 url 中存在 option 参数为 del_testcase 代表要删除用例
        if "nodeid" in request.args:
            # 利用 nodeid 参数指明要删除的用例
            nodeid = request.args.get("nodeid")
            # 查询用例后，进行删除
            testcase = TestCase.query.filter_by(nodeid=nodeid).first()
            db.session.delete(testcase)
            db.session.commit()
            return {"msg": "delete success"}

        # 批量删除
        # 删除多个用例，比如 '[nodeid_1, nodeid_2, nodeid_3]'
        # http://127.0.0.1:5000/testcase/delete?nodeids=nodeid_w1,nodeid_w2
        elif "nodeids" in request.args:
            # 利用 nodeid 参数指明要删除的用例
            nodeids = request.args.get("nodeids")
            # 查询用例后，进行删除
            for nodeid in nodeids.split(","):
                testcase = TestCase.query.filter_by(nodeid=nodeid).first()
                db.session.delete(testcase)
            db.session.commit()
            return {"msg": "delete success"}

class TestCaseUpdate(Resource):
    method_decorators = [auth.login_required]
    '''
    更新测试用例
    '''
    def post(self):
        request_body = request.json
        # 查询出要更新的数据
        testcase = TestCase.query.filter_by(nodeid=request_body.get("nodeid")).first()
        # 更新数据的描述信息
        testcase.description = request_body.get("description")
        db.session.commit()
        return {"msg": "update success"}


class TestCaseGet(Resource):
    method_decorators = [auth.login_required]
    def get(self):
        '''
        获取所有的测试用例数据
        :return:
        '''
        # option = request.args.get("option")
        # 1.先查找所有测试用例
        testcases = TestCase.query.all()
        # 2.对测试用例进行格式化
        format_test_cases = [i.as_dict() for i in testcases]
        return {"msg": "OK", "data": format_test_cases}


class TestCaseRun(Resource):
    method_decorators = [auth.login_required]

    def get(self):
        server = jenkins.Jenkins('http://127.0.0.1:8086/', username="admin", password="11b6f47797d686d6f723d932facef6e093")
        server.build_job("cekai17")
        return {"msg": "OK", "errcode": 200}