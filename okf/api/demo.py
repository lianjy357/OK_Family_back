from . import api
from okf import db, models
from okf.utils.response_code import send # 请求发送
import logging
@api.route('index')
def index():
    # logging.error('错误') # 记录错误信息
    # logging.warn('禁止') # 警告
    # logging.info('消息') # 消息
    # logging.debug('调试') # 调试
    return 'index page'

# 创建数据库
@api.route('/creatmodels')
def creatmodels():
    # 删除所有表
    db.drop_all()
    # 创建所有表
    db.create_all()
    return send(10000)