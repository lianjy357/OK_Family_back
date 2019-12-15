import json
# 配置文件

# 获取配置信息
with open("setting.json",'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
DBsetting = load_dict['SQLALCHEMY']
Redising = load_dict['REDIS']

class Config(object):
    """配置信息"""
    # 这个是用于session
    SECRET_KEY = "abcdefg"

    # 连接SQLALCHEMY数据库
    SQLALCHEMY_DATABASE_URI = DBsetting['URL'] # 数据库连接字符串
    SQLALCHEMY_TRACK_MODIFICATIONS = True # 数据库日志跟踪

    # # redis数据库配置
    # REDIS_HOST = Redising['REDIS_HOST']
    # REDIS_POST = Redising['REDIS_POST']

    # # flask_session配置
    # SESSION_TYPE = "redis"
    # # SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, post=REDIS_POST)
    # SESSION_USE_SIGNER = True # 对cookie中session_id进行隐藏处理
    # PERMANENT_SESSION_LIFETIME = 86400 # session数据有效期，单位秒

class DevelopmentConfig(Config):
    """开发环境"""
    DEBUG = True

class ProductConfig(Config):
    """生产环境"""
    pass

config_map = {
    "develop": DevelopmentConfig,
    "product": ProductConfig
}