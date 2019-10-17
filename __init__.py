from flask import Flask, render_template, request, Response
from flask_cors import CORS
import json

APP = Flask(__name__)

CORS(APP)

def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@APP.errorhandler(403)
def page_not_found_403(error):
    content = json.dumps({"error_code": "403"})
    resp = Response_headers(content)
    return resp

@APP.errorhandler(404)
def page_not_found_404(error):
    content = json.dumps({"error_code": "404"})
    resp = Response_headers(content)
    return resp

@APP.errorhandler(400)
def page_not_found_400(error):
    content = json.dumps({"error_code": "400"})
    resp = Response_headers(content)
    return resp

@APP.errorhandler(405)
def page_not_found_405(error):
    content = json.dumps({"error_code": "405"})
    resp = Response_headers(content)
    return resp

@APP.errorhandler(410)
def page_not_found_410(error):
    content = json.dumps({"error_code": "410"})
    resp = Response_headers(content)
    return resp

@APP.errorhandler(500)
def page_not_found_500(error):
    content = json.dumps({"error_code": "500"})
    resp = Response_headers(content)
    return resp

# 注册
from controller import apis