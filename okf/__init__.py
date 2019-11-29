from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf.csrf  import CSRFProtect
import redis
import logging
from logging.handlers import RotatingFileHandler

from config import config_map

# 创建数据库db对象
db = SQLAlchemy()

# 创建redis数据库连接对象
redis_store = None

def create_app(config_name):
    """创建flask应用对象"""
    app = Flask(__name__)
    # 获取参数
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
    
    db.init_app(app)

    # 初始化redis工具
    global redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_POST)

    # 利用flask_session， 将session数据保存到redis中
    Session(app)

    # 为flask补充csrf防护
    CSRFProtect(app)

    # 注册蓝图
    from . import api
    app.register_blueprint(api.api, url_prefix="/api/v1")

    # 配置日志信息
    # 配置日志的记录等级
    logging.basicConfig(level=logging.INFO)
    # 创建日志记录器，指明日志保存的路径，每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler('logs/log', maxBytes=1024*1024*100, backupCount=10, encoding='utf-8')
    # 创建日志记录格式：日志等级、输入日志信息的文件名、行数、日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s: %(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具独享（flask）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)

    return app