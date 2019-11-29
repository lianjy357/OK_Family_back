# -*- coding:utf-8 -*-
# run.py
from __init__ import create_app

if __name__ == '__main__':
    app = create_app()
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(debug=True, host='0.0.0.0')