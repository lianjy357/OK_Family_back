import records
import json
from werkzeug.security import generate_password_hash,check_password_hash

from utils import http

# 创建表的sql
# create_sql = """CREATE TABLE IF NOT EXISTS user_deo(
#   id int(11) PRIMARY KEY AUTO_INCREMENT,
#   name varchar(20),
#   age int
# )"""
# db.query(create_sql)

# 单条数据
# user = {"username": "yuze5", "password": 20, "nickname": "sally"}
# db.query('INSERT INTO sys_userInfo(username,password,nickname) values (:username, :password, :nickname)', **user)

# 多条数据
# users = [{"username": "yuze5", "password": 20, "nickname": "sally"},{"username": "yuze5", "password": 20, "nickname": "sally"}]
# db.bulk_query('INSERT INTO sys_userInfo(username,password,nickname) values (:username, :password, :nickname)', users)

# 请求数据库对象
class ASKDB:
    def __init__(self):
        # 获取配置信息
        with open("setting.json",'r', encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
        # 数据库连接
        DBsetting = load_dict['DB']
        self.db = records.Database('{0}+{1}://{2}:{3}@{4}:{5}/{6}'\
            .format(DBsetting['DatabaseType'], DBsetting['API'], DBsetting['Username'], DBsetting['Password'], DBsetting['IP'], DBsetting['Port'], DBsetting['DatabaseName']))
    
    '''
        保存数据insert（单条）
        输入：
        table_name: 库表名称
        database: 写入的数据
        输出：null
    '''
    def insert_one(self, table_name,database):
        try:
            # 获取Key值
            keys = database.keys()
            dbkeys = ",".join(str(i) for i in keys) # 数据库key值
            dbvalues = ",".join(':'+ str(i) for i in keys) # 数据库key值
            SQLling = 'INSERT INTO {0}({1}) values ({2})'\
                .format(table_name, dbkeys, dbvalues)
            take = self.db.query( SQLling, **database )
            print(take.all(as_dict=True))
        except:
            return [30001]
        else:
            return [10000]
    
    '''
        查询数据select（单条）
        输入：
        table_name: 库表名称
        condition: 查询条件（允许组合条件）
        输出：null
    '''
    def select_one(self, table_name, condition):
        try:
            SQLling = 'SELECT * FROM {0} WHERE {1}'\
                .format(table_name, condition)
            take = self.db.query( SQLling )
            return take.one() # 获取一条数据
        except:
            return [30001]
        else:
            return [10000]

# 整理成数据库请求结构
class mydb():
    # 注册用户信息
    def sys_userInfo_register(self, database):
        # 单条数据
        user = database
        getdb = ASKDB().insert_one('sys_userInfo',user)
        return http.send(getdb[0])
    # 登录用户获取信息
    def sys_userInfo_login(self, database):
        # 单条数据
        username = database['username']
        password = database['password']
        sqllang = "username='{0}'".format(username)
        getdb = ASKDB().select_one('sys_userInfo',sqllang)
        if getdb == None:
            return http.send(10002)
        if check_password_hash(getdb.password, password):
            dbData = dict(getdb)
            del dbData['password'] # 删除密码
            return http.send(10000, dbData)
        else:
            return http.send(10003)
    # 获取用户信息
    def sys_userInfo_get(self, database):
        # 单条数据
        username = database['username']
        sqllang = "username='{0}'".format(username)
        getdb = ASKDB().select_one('sys_userInfo',sqllang)
        if getdb == None:
            return http.send(10004)
        dbData = dict(getdb)
        del dbData['password'] # 删除密码
        return http.send(10000, dbData)
        