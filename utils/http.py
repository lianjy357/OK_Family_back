# -*- coding:utf-8 -*-
# http请求之后，对数据进行包装后再发出请求
from __init__ import Response_headers
import json

CODE = {
    # 请求成功
    10000: '操作成功',

    # 逻辑层异常
    10001: '验证码错误',
    # 10001: '用户不存在',
    # 10002: '帐号或密码错误',
    # 10003:'该帐号已被封禁',
    # 10004:'该角色已被封禁',
    # 10005:'包含不可操作用户',
    # 10006:'该记录已存在',
    # 10007:'机构封禁',
    # 10008:'邮箱格式错误',
    # 10009:'电话格式错误',
    # 10010:'角色帐号格式错误',

    # 请求层异常
    20001: '服务端链接超时',
    20002: 'ssl证书异常',

    # 数据库层异常
    30001: '保存失败',
    #系统层异常
    40001: '系统异常',
}

# 返回数据封装
def send(code,data=''):
    if data != '':
        return Response_headers(json.dumps({'code': code, 'data': data, 'msg': CODE[code]}))
    else:
        return Response_headers(json.dumps({'code': code, 'msg': CODE[code]}))
