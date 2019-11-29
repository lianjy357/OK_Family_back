# 数据库迁移
from datetime import datetime
from okf import db
# unique 唯一性  nullable 是否为空 onupdate 更新
class BaseModel(object):
    """模型基础，为每个模型补充创建时间和更新时间"""
    create_time = db.Column(db.DateTime, default=datetime.now) # 创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) # 更新时间

class User(BaseModel, db.Model):
    """用户表"""
    __tablename__ = "sys_user_profile"

    id = db.Column(db.Integer, primary_key=True) # 用户编号
    username = db.Column(db.String(32), unique=True, nullable=False) # 用户昵称
    password = db.Column(db.String(128), nullable=False) # 加密密码
    avatar_url = db.Column(db.String(128)) # 用户头像