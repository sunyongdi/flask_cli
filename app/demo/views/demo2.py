#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/12 10:44 上午
# software: PyCharm
"""
文件说明：
"""
from flask import request, make_response, session, url_for, redirect, current_app, g
from flask_restful import Resource

class Demo2(Resource):
    def post(self):
        user = request.args.get('user')
        if request.cookies.get('name') == 'syd':
            return '欢迎光临SYD'
        else:
            response = make_response('用户登录')
            if user == 'syd':
                response.set_cookie('name', user)
                return response
        return '不是用户'

    def get(self):
        g.name = request.args.get('name')
        session['logged_in'] = True
        # session.permanment = True 延长过期时间
        return redirect(url_for('api.demo1'))

# class Demo3(Resource):
#     def g

