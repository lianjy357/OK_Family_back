# -*- coding: utf-8 -*-
from okf import models, db
from okf.utils.response_code import send # 请求发送
# 注册
'''
    注册信息操作
    输入:用户信息，密码，邀请码
'''
def register(email, username, password, helloCode):
    # 效验判断
    if helloCode != '111111':
        return send(20101)
    # 写入数据库
    User = models.User(email, username, password, '')
    db.session.add(User)
    db.session.commit()
    return send(10000, '保存成功')