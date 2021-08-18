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

from app.v3.views.v3_demo import V3_demo

v3_blueprint = Blueprint('v3', __name__)
v3_blueprint_rest = Api(v3_blueprint)

v3_blueprint_rest.add_resource(V3_demo, '/demo')