# OK_Family_back

## python install

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
