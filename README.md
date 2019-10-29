# OK_Family_back

# python install
pip install

records
mysqlclient
pymysql

# configure
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
## 名词解析
DB：数据库配置

- DatabaseType：数据库类型
- API：API
- Username：数据库账号
- Password：数据库密码
- IP：地址
- Port：端口
- DatabaseName：数据库名