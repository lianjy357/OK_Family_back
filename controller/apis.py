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
    userName = data['userName']
    password = data['password']
    helloCode = data['helloCode'] if 'helloCode' in data else ""
    if helloCode != '000000':
        return http.send(10001)
    params = {
        'username': userName,
        'password': hash_password(password)
    }
    return mydb().sys_userInfo_register(params)
    

# 登录
@APP.route('/login',methods=['POST'])
def login():
    '''
        登录请求
    '''
    data = request.get_json()
    username = data['username']
    password = data['password']
    params = {
        'username': username,
        'password': password
    }
    return mydb().sys_userInfo_login(params)

# 获取用户信息
@APP.route('/getUserInfo',methods=['POST'])
def getUserInfo():
    '''
        获取用户信息
    '''
    data = request.get_json()
    username = data['username']
    password = data['password']
    params = {
        'username': username,
        'password': password
    }
    return mydb().sys_userInfo_get(params)
    
# 获取OKR信息
@APP.route('/getOKRInfo',methods=['GET'])
def getOKRInfo():
    '''
        获取OKR信息
    '''
    # data = request.get_json()
    # username = data['username']
    # password = data['password']
    params = {
        # 'username': username,
        # 'password': password
    }
    return mydb().okr_okr_get(params)