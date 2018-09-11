"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/5/1'
为真正的逻辑处理
"""

import tornado.web
from tornado.escape import json_decode
# 从commons中导入http_response方法
from common.commons import ( http_response, )
# 从配置文件中导入错误码
from conf.base import ( ERROR_CODE, )
class RegistHandle(tornado.web.RequestHandler):
    """handle /user/regist request
    :param phone: users sign up phone
    :param password: users sign up password
    :param code: users sign up code, must six digital code
    """
    def post(self):
        try:
            # 获取入参
            args = json_decode(self.request.body)
            phone = args['phone']
            password = args['password']
            verify_code = args['code']
        except:
            # 获取入参失败时，抛出错误码及错误信息
            http_response(self, ERROR_CODE['1001'], 1001)
            return
        # 处理成功后，返回成功码“0”及成功信息“ok”
        http_response(self, ERROR_CODE['0'], 0)