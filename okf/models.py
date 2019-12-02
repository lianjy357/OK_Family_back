# 数据库迁移
from datetime import datetime
from okf import db
# unique 唯一性  nullable 是否为空 onupdate 更新
class BaseModel(object):
    """模型基础，为每个模型补充创建时间和更新时间"""
    _time = db.Column(db.DateTime, default=datetime.now) # 创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) # 更新时间

class User(BaseModel, db.Model):
    """用户表"""
    __tablename__ = "sys_user_profile"

    id = db.Column(db.Integer, primary_key=True) # 用户编号
    username = db.Column(db.String(32), unique=True, nullable=False) # 用户昵称
    password = db.Column(db.String(128), nullable=False) # 加密密码
    avatar_url = db.Column(db.String(128)) # 用户头像
    organization = db.relationship("Organization", backref="sys_user_profile") # 用户下拥有的组织

class Organization(BaseModel, db.Model):
    """组织表"""
    __tablename__ = "sys_organization"

    id = db.Column(db.Integer, primary_key=True) # 组织编号
    name = db.Column(db.String(64), nullable=False) # 组织名称
    admin_id = db.Column(db.Integer, db.ForeignKey("sys_user_profile.id"), nullable=False) # 组织管理者
    person = db.relationship("User", backref="sys_user_profile") # 组织下拥有的成员
    oid = db.relationship("OKR_O", backref="sys_organization") # 组织下拥有的OKR的O

class OKR_O(BaseModel, db.Model):
    """OKR_O"""
    __tablename__ = "okr_o"

    id = db.Column(db.Integer, primary_key=True) # 编号
    type = db.Column(db.Integer, nullable=False) # OKR类型（0成员，1家庭）
    title = db.Column(db.String(64), nullable=False) # 标题
    description = db.Column(db.String(255)) # 描述
    startdate = db.Column(db.DateTime) # 创建时间
    enddate = db.Column(db.DateTime) # 创建时间
    progress = db.Column(db.Integer) # 进度
    createuser = db.Column(db.Integer, db.ForeignKey("sys_user_profile.id"), nullable=False) # 创建的人员
    person = db.relationship("User", backref="sys_user_profile") # OKR负责的成员
    krid = db.relationship("OKR_KR", backref="okr_o") # O下拥有的kr
    state = db.Column(db.Integer, nullable=False) # 状态（0关，1开）

    
class OKR_KR(BaseModel, db.Model):
    """OKR_KR"""
    __tablename__ = "okr_kr"

    id = db.Column(db.Integer, primary_key=True) # 编号
    title = db.Column(db.String(64), nullable=False) # 标题
    progress = db.Column(db.Integer) # 进度
    type = db.Column(db.String(64), nullable=False) # 类型（NUM数字型、PER百分比型）
    startnum = db.Column(db.Integer, nullable=False) # 起始值
    endnum = db.Column(db.Integer, nullable=False) # 目标值
    confidencenum = db.Column(db.Integer, nullable=False) # 信心值