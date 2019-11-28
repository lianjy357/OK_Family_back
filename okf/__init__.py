from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf.csrf  import CSRFProtect
import redis

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
    redis_store = redis.StrictRedis((host=config_class.REDIS_HOST, post=config_class.REDIS_POST))

    # 利用flask_session， 将session数据保存到redis中
    Session(app)

    # 为flask补充csrf防护
    CSRFProtect(app)

    return app