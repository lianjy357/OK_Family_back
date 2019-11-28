# from __init__ import APP
# from __init__ import render_template, request, Response
from utils import http
from werkzeug.security import generate_password_hash,check_password_hash

import json

from database.OK_mysql import mydb

# 进入程序
def init_app(app):

    # 密码hash
    def hash_password(password):
        return generate_password_hash(password)
    # 密码匹配()
    def verify_password(password, password_hash):
        return check_password_hash(password, password_hash) # True or False

    # @app.route("/")
    # def home():
    # return render_template('index.html')

    # 注册
    @app.route('/register',methods=['POST'])
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
    @app.route('/login',methods=['POST'])
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
    @app.route('/getUserInfo',methods=['POST'])
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
    @app.route('/getOKRInfo',methods=['GET'])
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

    # 保存OKR信息
    @app.route('/saveOKRInfo',methods=['POST'])
    def saveOKRInfo():
        '''
            获取OKR信息
        '''
        data = request.get_json()
        
        # username = data['username']
        # password = data['password']
        params = {
            'type': data['type'],
            'title': data['title'],
            'description': data['description'],
            'startdate': data['startDate'],
            'enddate': data['endDate'],
            'progress': data['progress'],
            'person': str(data['person']),
            'type': data['type'],
            'username': data['username'],
            'KR': data['KR']
        }
        return mydb().okr_okr_save(params)

    # 修改OKR进度
    @app.route('/updataOKRprogress',methods=['POST'])
    def updataOKRprogress():
        '''
            修改OKR进度
        '''
        data = request.get_json()
        # username = data['username']
        # password = data['password']
        kr = []
        for krdata in data['KR']:
            par = {
                'id': krdata['id'],
                'progress': krdata['progress'],
                'confidenceNum': krdata['confidenceNum']
            }
            kr.append(par)
        params = {
            'ranid': data['ranid'],
            'KR': kr
        }
        return mydb().okr_okrprogress_updata(params)

    # 删除OKR
    @app.route('/deleteOKR',methods=['POST'])
    def deleteOKR():
        '''
            修改OKR进度
        '''
        data = request.get_json()
        
        params = {
            'ranid': data['ranid']
        }
        return mydb().okr_okr_delete(params)