# -*- coding:utf-8 -*-
# run.py
from __init__ import APP

if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix
    APP.wsgi_app = ProxyFix(APP.wsgi_app)
    APP.run(debug=False, host='0.0.0.0')