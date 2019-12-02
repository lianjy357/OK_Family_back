# -*- coding: utf-8 -*-
# 用户操作的接口
from . import api # api对象

from okf import redis_store # redis
from flask import request # 请求接收
from okf.utils.response_code import send # 请求发送


@api.route('/register', methods=['POST'])
def register():
    '''注册'''
    print('进入等等')
    # 获取参数
    req_dict = request.get_json()
    userName = req_dict.get('userName')
    password = req_dict.get('password')
    helloCode = req_dict.get('helloCode')
    # 效验参数
    if not all([userName, password, helloCode]):
        return send(20001)
    return send(10000)