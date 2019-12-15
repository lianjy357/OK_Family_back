# OK_Family_back

## python install

### 虚拟环境外

pip install
virtualenv

### 虚拟环境内(第一版)

pip install

flask
flask_cors
records
mysqlclient
pymysql
passlib
flask_httpauth
itsdangerous
uwsgi
redis
flask_sqlalchemy
flask_wtf
flask_session
flask_script
flask_migrate

### 虚拟环境内(第二版)

pip install

flask
flask_cors
uwsgi
redis
pymysql
mysqlclient
flask_sqlalchemy
flask_wtf
flask_session
flask_script
flask_migrate

## configure

需要在根目录新建一个文件`setting.json`
将必要的数据填入其中

```json
{
    "DB": {
        "DatabaseType": "mysql",
        "API": "pymysql",
        "Username": "root",
        "Password": "",
        "IP": "",
        "Port": "",
        "DatabaseName": ""
    }
}
```

### 名词解析

DB：数据库配置

- DatabaseType：数据库类型
- API：API
- Username：数据库账号
- Password：数据库密码
- IP：地址
- Port：端口
- DatabaseName：数据库名

## 文件夹结构描述

- `controller` 所有需要被控制的内容
  - `apis.py` 只作为数据接收，只处理一些简单的数据请求问题，将所有逻辑交给
- `database` 所有的数据库请求
  - `OK_mysql.py` 数据库配置信息

## 运行虚拟环境

创建虚拟环境
`virtualenv venv`
启动
旧版本需要加source
`source venv/bin/activate`
新版本
`venv/bin/activate`
退出
`deactivate`

## 更新数据库操作方法

python app.py db migrate
python app.py db upgrade