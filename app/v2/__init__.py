#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/18 5:08 下午
# software: PyCharm
"""
文件说明：
"""
from flask_restful import Api
from flask import Blueprint

from app.v2.views.v2_demo import V2_Demo

v2_blueprint = Blueprint('v2', __name__)
v2_blueprint_rest = Api(v2_blueprint)

v2_blueprint_rest.add_resource(V2_Demo, '/demo')
