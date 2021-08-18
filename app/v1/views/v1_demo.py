#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/18 5:28 下午
# software: PyCharm
"""
文件说明：
"""
from flask_restful import Resource

class V1_demo(Resource):
    def get(self):
        return 'v1_demo'