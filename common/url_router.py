"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/5/1'
"""
from __future__ import unicode_literals
from importlib import import_module
def include(module):
    '''
    根据传入的字符串，调用相应的模块,如 module 为字符串 regist 时，
    调用views.users.users_views.RegistHandle 模块
    '''
    res = import_module(module)
    urls = getattr(res, 'urls', res)
    return urls

def url_wrapper(urls):
    '''
    拼接请求 url，调用对应的模块，如拼接 users 和 regist 成 url /users/regist，
    调用 views.users.users_views.RegistHandle 模块
    '''
    wrapper_list = []
    for url in urls:
        path, handles = url
        if isinstance(handles, (tuple, list)):
            for handle in handles:
                #分离获取字符串（如regist）和调用类（如views.users.users_views.RegistHandle）
                pattern, handle_class = handle
                #拼接url，新的url调用模块
                wrap = ('{0}{1}'.format(path, pattern), handle_class)
                wrapper_list.append(wrap)
        else:
            wrapper_list.append((path, handles))
    return wrapper_list