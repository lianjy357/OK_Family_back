import records
import json




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

# 数据库对象
class mydb():
    def __init__(self):
        # 获取配置信息
        with open("setting.json",'r', encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
        # 数据库连接
        DBsetting = load_dict['DB']
        self.db = records.Database('{0}+{1}://{2}:{3}@{4}:{5}/{6}'\
            .format(DBsetting['DatabaseType'], DBsetting['API'], DBsetting['Username'], DBsetting['Password'], DBsetting['IP'], DBsetting['Port'], DBsetting['DatabaseName']))
    def sys_userInfo(self, database):
        # 单条数据
        user = database
        self.db.query('INSERT INTO sys_userInfo(username,password) values (:userName, :password)', **user)
        return database