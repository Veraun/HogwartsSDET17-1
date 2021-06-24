'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: user_table.py
@time: 2021/5/24 09:50
@Email: Warron.Wang
'''

import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 用于生成具有时间维护的token
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature, SignatureExpired

from backend.backend_server import app, db




# 使用db，可以让类映射到数据库中的User表
class User(db.Model):
    '''
    用户表：需要有账号、密码、邮箱

    '''
    # 以下字段代表 数据库中的表头
    id = db.Column(db.Integer, primary_key=True)  # 主键，唯一标识，类似身份证
    username = db.Column(db.String(80), unique=True, nullable=False)  # 唯一；必填项
    password = db.Column(db.String(80), unique=False, nullable=False)  # 不唯一；必填项
    email = db.Column(db.String(120), unique=False, nullable=False)

    # TODO 后续新增字段
    # 创建日期、注册时间

    def __repr__(self):
        return f'<User {self.username}>'

    def generate_token(self, expires_in=3 * 3600):
        '''
        生成 token
        :return:
        '''
        # expires_in 代表超时时间
        # app.config['SECRETY_KEY']：token种子，用于生成token，其值是可以随机的
        serializer = TimedJSONWebSignatureSerializer(app.config['SECRETY_KEY'], expires_in=expires_in)
        token_id = self.username + self.password + str(datetime.datetime.now())
        # dumps 用于序列化(把python对象转换成字符串)，生成token
        token = serializer.dumps({"id": self.id, "token_id": token_id}).decode()  # 进行解码
        return token

    # 方便外界进行调用，同时此方法不会用到对象中的数据
    @classmethod
    def check_token(cls, token):
        '''
        校验token
        :return: User or None
        '''
        serializer = TimedJSONWebSignatureSerializer(app.config['SECRETY_KEY'])
        try:
            # loads 用于反序列化(把token转换成python对象)
            token_loads_result = serializer.loads(token)
        # 如果 token 校验失败，会抛出BadSignature
        # 如果 token 超时，会抛出SignatureExpired
        except (BadSignature, SignatureExpired):
            return None
        # User.query.get表示利用id找到User表的字段对象
        return User.query.get(token_loads_result["id"])


# class Task(db.Model):
#     task_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#
#     def __repr__(self):
#         return '<Task %r>' % self.name


if __name__ == '__main__':
    # pass
    # 删库
    db.drop_all()

    # 在远程数据库中创建表
    db.create_all()

    # -----------------------------添加
    # 数据库的添加操作
    # 1.向User表插入数据  实例化User类
    # for i in range(1, 20):
    #     data = User(username="zhangsan" + str(i), description='i am zhangsan ')
    # 2.把类添加到SQLAlchemy
    #     db.session.add(data)
    # 3.把操作提交
    # db.session.commit()

    # -----------------------------查询
    # 数据库的查询操作
    # 在User表中查数据，就使用User.query
    # User.query.all()  # all指获取所有结果
    # result = User.query.filter_by(description=123).first()  # first指获取第一个结果
    # result = User.query.filter_by(description='i am zhangsan').all()   # all指获取所有结果
    # result = User.query.filter_by(id=2, description='i am zhangsan').all()  # 多个条件联合查询for
    # result = User.query.all()
    # result = [i for i in result if "0" in i.username]
    # print(result)

    # -----------------------------更新
    # 先过滤想要修改的数据，然后对数据进行修改，修改完成后使用commit()进行提交
    # user = User.query.filter_by(username='zhangsan1').first()
    # print(type(user))
    # user.description = "hello"
    # db.session.commit()

    # -----------------------------删除
    # 先过滤想要修改的数据，利用delete()进行删除，最后使用commit()进行提交
    # user = User.query.filter_by(username='zhangsan1').first()
    # db.session.delete(user)
    # db.session.commit()
