# 数据库迁移
from datetime import datetime
from okf import db
# unique 唯一性  nullable 是否为空 onupdate 更新
class BaseModel(object):
    """模型基础，为每个模型补充创建时间和更新时间"""
    create_time = db.Column(db.DateTime, default=datetime.now) # 创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) # 更新时间

# 多对多用户与组织表
User_Organization = db.Table('User_Organization', 
    db.Column('user_id', db.Integer, db.ForeignKey('User.id')),
    db.Column('organization_id', db.Integer, db.ForeignKey('Organization.id'))
)

class User(BaseModel, db.Model):
    """用户表"""
    # 设置对应的数据表名称（建议与模型类名称一致）
    __tablename__ = "User"

    # 设置表的字段（类变量）
    id = db.Column(db.Integer, primary_key=True) # 用户编号
    email = db.Column(db.String(128), nullable=False) # 用户邮箱
    username = db.Column(db.String(32), unique=True, nullable=False) # 用户昵称
    password = db.Column(db.String(128), nullable=False) # 加密密码
    avatar_url = db.Column(db.String(128)) # 用户头像

    # 创建构造方法，为类变量赋值
    def __init__(self, username, password, avatar_url):
        self.username = username
        self.password = password
        self.avatar_url = avatar_url
    
    # 创建对象输出的方法(测试用的)
    def __repr__(self):
        return 'User: [{0},{1}]'.format(self.id, self.username)

class Organization(BaseModel, db.Model):
    """组织表"""
    __tablename__ = "Organization"

    id = db.Column(db.Integer, primary_key=True) # 组织编号
    name = db.Column(db.String(64), nullable=False) # 组织名称
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"), nullable=False) # 组织拥有者
    user = db.relationship("User", secondary = User_Organization, backref = db.backref("Organization")) # 组织与用户多对多关联
    

    # 创建构造方法，为类变量赋值
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
    
    # 创建对象输出的方法(测试用的)
    def __repr__(self):
        return 'Organization: [{0},{1}]'.format(self.id, self.name)

class OKR_O(BaseModel, db.Model):
    """OKR_O"""
    __tablename__ = "OKR_O"

    id = db.Column(db.Integer, primary_key=True) # 编号
    otype = db.Column(db.Integer, nullable=False) # OKR类型（0成员，1家庭）
    title = db.Column(db.String(64), nullable=False) # 标题
    description = db.Column(db.String(255)) # 描述
    startdate = db.Column(db.DateTime) # 开始时间
    enddate = db.Column(db.DateTime) # 创建时间
    progress = db.Column(db.Integer) # 进度
    createuser = db.Column(db.Integer, db.ForeignKey("User.id"), nullable=False) # 创建的人员
    person = db.relationship("User", backref="User") # OKR负责的成员
    krid = db.relationship("OKR_KR", backref="OKR_O") # O下拥有的kr
    state = db.Column(db.Integer, nullable=False) # 状态（0关，1开）
    organization_id = db.Column(db.Integer, db.ForeignKey("Organization.id"), nullable=False)
    organization = db.relationship("Organization", backref="OKR_O") # 组织下拥有的OKR的O

    # 创建构造方法，为类变量赋值
    def __init__(self, otype, title, description, startdate, enddate, progress, createuser, person, krid, state):
        self.otype = otype
        self.title = title
        self.description = description
        self.startdate = startdate
        self.enddate = enddate
        self.progress = progress
        self.createuser = createuser
        self.person = person
        self.krid = krid
        self.state = state
    
    # 创建对象输出的方法(测试用的)
    def __repr__(self):
        return 'OKR_O: [{0},{1}]'.format(self.id, self.otype)

    
class OKR_KR(BaseModel, db.Model):
    """OKR_KR"""
    __tablename__ = "OKR_KR"

    id = db.Column(db.Integer, primary_key=True) # 编号
    title = db.Column(db.String(64), nullable=False) # 标题
    progress = db.Column(db.Integer) # 进度
    krtype = db.Column(db.String(64), nullable=False) # 类型（NUM数字型、PER百分比型）
    startnum = db.Column(db.Integer, nullable=False) # 起始值
    endnum = db.Column(db.Integer, nullable=False) # 目标值
    confidencenum = db.Column(db.Integer, nullable=False) # 信心值
    okr_o_id = db.Column(db.Integer, db.ForeignKey("OKR_O.id"), nullable=False)
    okr_o = db.relationship("OKR_O", backref="OKR_KR") # 组织下拥有的OKR的KR

    # 创建构造方法，为类变量赋值
    def __init__(self, title, progress, krtype, startnum, endnum, confidencenum):
        self.title = title
        self.progress = progress
        self.krtype = krtype
        self.startnum = startnum
        self.endnum = endnum
        self.confidencenum = confidencenum
    
    # 创建对象输出的方法(测试用的)
    def __repr__(self):
        return 'OKR_KR: [{0},{1}]'.format(self.id, self.title)