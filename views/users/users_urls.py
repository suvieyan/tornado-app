"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/5/1'
处理针对 users 相关的路由及调用类之间的路由
"""
from __future__ import unicode_literals
from .users_views import (
    RegistHandle
)
urls = [
    #从 /users/regist 过来的请求，将调用 users_views 里面的 RegistHandle 类
    (r'regist', RegistHandle)
]

