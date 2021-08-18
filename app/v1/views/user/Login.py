#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/18 5:01 下午
# software: PyCharm
"""
文件说明：
"""
from flask_restful import Resource


class Login(Resource):
    """
    用户认证
    """
    def get(self):
        return {
                   'err': '',
                   'msg': 'ok'
               }, 200
