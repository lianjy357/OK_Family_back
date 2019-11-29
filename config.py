import json
# 配置文件

# 获取配置信息
with open("setting.json",'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
DBsetting = load_dict['DB']

class Config(object):
    """配置信息"""
    # 这个是用于session
    SECRET_KEY = "abcdefg"
    
    # 连接records数据库
    SQL_URL = '{0}+{1}://{2}:{3}@{4}:{5}/{6}'\
            .format(DBsetting['DatabaseType'], DBsetting['API'], DBsetting['Username'], DBsetting['Password'], DBsetting['IP'], DBsetting['Port'], DBsetting['DatabaseName'])

    # redis数据库配置
    REDIS_HOST = "127.0.0.1"
    REDIS_POST = 6379

    # flask_session配置
    SESSION_TYPE = "redis"
    # SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, post=REDIS_POST)
    SESSION_USE_SIGNER = True # 对cookie中session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400 # session数据有效期，单位秒

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