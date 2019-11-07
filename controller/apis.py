from __init__ import APP
from __init__ import render_template, request, Response
from utils import http
from werkzeug.security import generate_password_hash,check_password_hash

import json

from database.OK_mysql import mydb


# 密码hash
def hash_password(password):
    return generate_password_hash(password)
# 密码匹配()
def verify_password(password, password_hash):
    return check_password_hash(password, password_hash) # True or False

@APP.route("/")
def home():
  return render_template('index.html')

# 注册
@APP.route('/register',methods=['POST'])
def register():
    '''
        注册请求
    '''
    data = request.get_json()
    print(data)
    userName = data['userName']
    password = data['password']
    helloCode = data['helloCode'] if 'helloCode' in data else ""
    if helloCode != '000000':
        return http.send(10001)
    
    params = {
        'username': userName,
        'password': hash_password(password)
    }
    OKdb = mydb()
    return OKdb.sys_userInfo(params)
    

# 登录
@APP.route('/login',methods=['POST'])
def login():
    '''
        登录请求
    '''
    
    # data = request.get_json()
    # dirs = data['dir']
    # name = data['name']
    OKdb = mydb()
    outdata = OKdb.sys_userInfo('数据data')
    return Response_headers(json.dumps({'data':outdata}))