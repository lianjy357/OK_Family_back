from __init__ import APP
from __init__ import render_template, request, Response
from __init__ import Response_headers
from database.OK_mysql import mydb
import json

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
    helloCode = data['helloCode']
    if helloCode != '000000':
        return Response_headers(json.dumps({'data':'邀请码错误'}))
    OKdb = mydb()
    outdata = OKdb.sys_userInfo({'userName': userName, 'password': password})
    return Response_headers(json.dumps({'data':outdata}))

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