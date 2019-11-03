import records
import json

# 获取配置信息
with open("setting.json",'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
    

# 数据库连接
DBsetting = load_dict['DB']
db = records.Database('{0}+{1}://{2}:{3}@{4}:{5}/{6}'\
  .format(DBsetting['DatabaseType'], DBsetting['API'], DBsetting['Username'], DBsetting['Password'], DBsetting['IP'], DBsetting['Port'], DBsetting['DatabaseName']))

# 创建表的sql
# create_sql = """CREATE TABLE IF NOT EXISTS user_deo(
#   id int(11) PRIMARY KEY AUTO_INCREMENT,
#   name varchar(20),
#   age int
# )"""
user = [{"username": "yuze5", "password": 20, "nickname": "sally"},{"username": "yuze5", "password": 20, "nickname": "sally"}]
# print('INSERT INTO sys_userInfo(username,password,nickname) values (:username, :password, :nickname)', **user)
db.bulk_query('INSERT INTO sys_userInfo(username,password,nickname) values (:username, :password, :nickname)', user)

print('创建成功')

## 执行
# db.query(create_sql)