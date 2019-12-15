# -*- coding: utf-8 -*-
from okf import models, db
from okf.utils.response_code import send # 请求发送
# 注册
def register(username,password):
    # 写入数据库
    User = models.User(username, password, '')
    db.session.add(User)
    db.session.commit()
    return send(10000, '保存成功')