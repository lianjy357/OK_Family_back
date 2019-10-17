from __init__ import APP
from __init__ import render_template, request, Response
from __init__ import Response_headers
import json

@APP.route("/")
def home():
  return render_template('index.html')

# 登录请求
@APP.route('/login',methods=['POST'])
def run():
    '''
        登录请求
    '''
    # data = request.get_json()
    # dirs = data['dir']
    # name = data['name']
    outdata = 'hello world！'
    return Response_headers(json.dumps({'data':outdata}))