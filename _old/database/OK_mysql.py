import records
import json
import random
import string
from werkzeug.security import generate_password_hash,check_password_hash

# from utils import http

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
            dbvalues = ",".join(':'+ str(i) for i in keys) # 数据库value值
            SQLling = 'INSERT INTO {0}({1}) values ({2})'\
                .format(table_name, dbkeys, dbvalues)
            take = self.db.query( SQLling, **database )
            # return take.one()
        except Exception as ex:
            print("出现如下异常%s"%ex)
            return 30001
        else:
            return 10000

    '''
        保存数据insert（多条）
        输入：
        table_name: 库表名称
        database: 写入的数据
        输出：null
    '''
    def insert_all(self, table_name,database):
        try:
            # 获取Key值
            keys = database[0].keys()
            dbkeys = ",".join(str(i) for i in keys) # 数据库key值
            dbvalues = ",".join(':'+ str(i) for i in keys) # 数据库value值
            SQLling = 'INSERT INTO {0}({1}) values ({2})'\
                .format(table_name, dbkeys, dbvalues)
            self.db.bulk_query( SQLling, database )
        except Exception as ex:
            print("出现如下异常%s"%ex)
            return 30001
        else:
            return 10000
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
            return 30002
        else:
            return 10000

    '''
        查询数据select（多条,一对多结构）
        输入：
        select_name: 输出查询结果
        table_name: 库表名称（多库表，逗号隔开）
        condition: 查询条件及其关联条件（允许组合条件）
        输出：null
    '''
    def select_all(self, select_name, table_name, condition):
        try:
            if (condition != ''):
                condition = 'WHERE '+ condition
            SQLling = 'SELECT {0} FROM {1} {2}'\
                .format(select_name, table_name, condition)
            take = self.db.query( SQLling )
            return take.all(as_dict=True) # 获取所有数据
        except Exception as ex:
            print("出现如下异常%s"%ex)
            return 30002
        else:
            return 10000
    '''
        更新数据update（单条）
        输入：
        table_name: 库表名称
        updata_date: 需要修改的内容（允许多个参数）
        condition: 查询条件（允许组合条件）
        输出：null
    '''
    def update_one(self, table_name, updata_date, condition):
        try:
            SQLling = 'UPDATE {0} SET {1} WHERE {2}'\
                .format(table_name, updata_date, condition)
            take = self.db.query( SQLling )
        except Exception as ex:
            print("出现如下异常%s"%ex)
            return 30002
        else:
            return 10000
    '''
        删除数据delete（单条）
        输入：
        table_name: 库表名称
        condition: 查询条件（允许组合条件）
        输出：null
    '''
    def delete_one(self, table_name, condition):
        try:
            SQLling = 'DELETE FROM {0} WHERE {1}'\
                .format(table_name, condition)
            take = self.db.query( SQLling )
        except Exception as ex:
            print("出现如下异常%s"%ex)
            return 30002
        else:
            return 10000

# 整理成数据库请求结构
class mydb():
    # 注册用户信息
    def sys_userInfo_register(self, database):
        # 单条数据
        user = database
        getdb = ASKDB().insert_one('sys_userInfo',user)
        return http.send(getdb)
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
    # 获取OKR信息
    def okr_okr_get(self, database):
        # username = database['username']
        # sqllang = "username='{0}'".format(username)
        # sqllang = "okr_objectives.id=okr_keyresults.oid".format(username)
        getdb = ASKDB().select_all('*','okr_objectives', '')
        if (getdb == 30002):
            return http.send(30002)
        # 再次查表获取KR信息
        for o in getdb:
            getkrdb = ASKDB().select_all('*','okr_keyresults', "ranid='%s'"%(o['ranid']))
            o['KR'] = getkrdb
        return utils.http.send(10000, getdb)
    # 创建OKR信息
    def okr_okr_save(self, database):
        # 单条数据
        ranid = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        kr = database.pop('KR')
        for item in kr:
            item['ranid'] = ranid
        o = database
        database['ranid'] = ranid
        getdb = ASKDB().insert_one('okr_objectives',o)
        if (getdb == 30001):
            return http.send(30001)
        getdb = ASKDB().insert_all('okr_keyresults',kr)
        if (getdb == 30001):
            return http.send(30001)
        return http.send(10000)
    # 修改OKR进度
    def okr_okrprogress_updata(self, database):
        krpronum = 0 # kr进度总数
        krnum = 0 # kr个数
        for kr in database['KR']:
            ASKDB().update_one('okr_keyresults', "progress='%f',confidenceNum='%s'"%(float(kr['progress']),kr['confidenceNum']), "id='%f'"%(kr['id']))
            krpronum = krpronum + float(kr['progress'])
            krnum = krnum + 1
        getdb = ASKDB().update_one('okr_objectives',"progress='%s'"%(str(krpronum / krnum)), "ranid='%s'"%(database['ranid']))
        if (getdb == 30001):
            return http.send(30001)
        return http.send(10000)
    # 删除OKR
    def okr_okr_delete(self, database):
        ASKDB().delete_one('okr_keyresults', "ranid='%s'"%(database['ranid']))
        getdb = ASKDB().delete_one('okr_objectives', "ranid='%s'"%(database['ranid']))
        if (getdb == 30001):
            return http.send(30001)
        return http.send(10000)
        