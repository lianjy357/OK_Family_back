# -*- coding:utf-8 -*-

"""
错误代码说明
编码：20502
2：服务级错误（1为系统级错误）
05：服务模块代码
02：具体错误代码
"""
from flask import Response
import datetime
import json

CODE = {
    # 请求成功
    10000: 'success',

    # 系统级错误
    10001: '系统错误',

    # 服务级错误
    # 通用层
    20001: '请求参数不完整',
    # 用户层
    20101: '验证码错误',
    20102: '用户不存在',
    20103: '密码错误',
    20104: '获取用户信息失败',
}
# 时间处理
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self,obj)

# 包装发送请求
def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

# 返回数据封装（最终调用此函数即可）
def send(code,data=''):
    if data != '':
        return Response_headers(json.dumps({'code': code, 'data': data, 'msg': CODE[code]},cls=DateEncoder))
    else:
        return Response_headers(json.dumps({'code': code, 'msg': CODE[code]}))
