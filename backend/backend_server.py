'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: backend_server.py
@time: 2021/5/24 15:09
@Email: Warron.Wang
'''

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
# 配置数据库的详细信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@host:port/test_backend_17'
# 初始化一个db
db = SQLAlchemy(app)

# 将flask实例加载到flask-restful中
api = Api(app)


# 使用db，可以让类映射到数据库中的User表
class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键，唯一标识，类似身份证
    nodeid = db.Column(db.String(80), unique=True, nullable=False)  # 唯一；必填项
    description = db.Column(db.String(120), unique=False, nullable=True)

    def as_dict(self):
        '''
        返回测试用例的数据
        :return:
        '''
        return {'id': self.id, "nodeid": self.nodeid, "description":self.description}


# 定义测试用例接口
class TestCaseAdd(Resource):
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
    # get 方法代表接收get请求
    def get(self):
        '''
        删除测试用例
        :return:
        '''
        # http://127.0.0.1:5000/testcase/delete?nodeid=nodeid_w1
        if "nodeid" in request.args:
            # 利用 nodeid 参数指明要删除的用例
            nodeid = request.args.get("nodeid")
            # 查询用例后，进行删除
            testcase = TestCase.query.filter_by(nodeid=nodeid).first()
            db.session.delete(testcase)
            db.session.commit()
            return {"msg": "delete success"}

        # 批量删除
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
        return format_test_cases


# 添加到 flask-restful 中，并增加路由
api.add_resource(TestCaseAdd, '/testcase/add')
api.add_resource(TestCaseDelete, '/testcase/delete')
api.add_resource(TestCaseUpdate, '/testcase/update')
api.add_resource(TestCaseGet, '/testcase/get')

if __name__ == '__main__':
    app.run(debug=True)

    # 删库
    # db.drop_all()

    # 在远程数据库中创建表
    # db.create_all()

    # for i in range(30):
    #     data = TestCase(nodeid="nodeid_" + str(i))
    #     db.session.add(data)
    # db.session.commit()
