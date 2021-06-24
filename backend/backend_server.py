'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: backend_server.py
@time: 2021/5/24 15:09
@Email: Warron.Wang
'''
from flask_cors import CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
# 配置数据库的详细信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@host:port/test_backend_17'
# 初始化一个db
db = SQLAlchemy(app)

# 将flask实例加载到flask-restful中
api = Api(app)

# flask 解决跨域问题、使用 CORS 解决同源问题
CORS(app)

# 配置token种子
app.config['SECRETY_KEY'] = "warron2kily"

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


def router():
    from backend.api.testcase import TestCaseAdd
    api.add_resource(TestCaseAdd, '/testcase/add')
    from backend.api.testcase import TestCaseDelete
    api.add_resource(TestCaseDelete, '/testcase/delete')
    from backend.api.testcase import TestCaseUpdate
    api.add_resource(TestCaseUpdate, '/testcase/update')
    from backend.api.testcase import TestCaseGet
    api.add_resource(TestCaseGet, '/testcase/get')
    from backend.api.login import Login
    api.add_resource(Login, '/login')
    from backend.api.testcase import TestCaseRun
    api.add_resource(TestCaseRun, '/testcase/run')
    from backend.api.logout import Logout
    api.add_resource(Logout, '/logout')


if __name__ == '__main__':
    router()
    app.run(debug=True)

    # 删库
    # db.drop_all()

    # 在远程数据库中创建表
    # db.create_all()

    # for i in range(30):
    #     data = TestCase(nodeid="nodeid_" + str(i))
    #     db.session.add(data)
    # db.session.commit()
