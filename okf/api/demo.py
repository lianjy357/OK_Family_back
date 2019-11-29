from . import api
from okf import db, models
import logging
@api.route('index')
def index():
    # logging.error('错误') # 记录错误信息
    # logging.warn('禁止') # 警告
    # logging.info('消息') # 消息
    # logging.debug('调试') # 调试
    return 'index page'