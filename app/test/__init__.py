#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/18 5:20 下午
# software: PyCharm
"""
文件说明：
"""

from flask_restful import Api
from flask import Blueprint

test_blueprint = Blueprint('test', __name__)
v1_blueprint_rest = Api(test_blueprint)
