from flask import g, session
from flask_restful import Resource



class Logout(Resource):
    # auth.login_required 是 httpAuth 的用法，添加了此装饰器的对象会回调校验方法
    # method_decorators 代表给 Login 接口添加一个装饰器，下面的 get 表示对 get 接口进行添加

    def get(self):
        session.clear()
        return {"msg":"success"}

