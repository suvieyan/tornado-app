"""
__title__ = ''
__author__ = 'Yan'
__mtime__ = '2018/5/1'
"""

import json
def http_response(self, msg, code):
    self.write(json.dumps({"data": {"msg": msg, "code": code}}))

if __name__ == "__main__":
    http_response()