#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/17 5:58 下午
# software: PyCharm
"""
文件说明：
"""
from flask_restful import Resource
from flask import current_app, request

class Demo_redis(Resource):
    def post(self):
        s = request.form.get('redis_key')
        r = current_app.redis_pool
        r.set('food', s, ex=3)
        return {
            'result': r.get('food')
        }