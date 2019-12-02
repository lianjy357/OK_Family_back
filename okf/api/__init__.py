# -*- coding: utf-8 -*-
from flask import Blueprint

# 创建蓝图对象
api = Blueprint('api', __name__)

# 导入蓝图的视图，让程序知道在api包下有个demo.py文件
from . import demo # 测试接口
from . import user # 用户接口