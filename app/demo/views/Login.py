#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/8 12:41 下午
# software: PyCharm
"""
文件说明：
"""

from flask_restful import Resource
from flask import jsonify
from framework.utils.forms import LoginForm
from app.demo.models.User import User
from flask_login import login_user


class Login(Resource):
    """登录界面"""
    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(name=form.username.data).first()
            if user:
                if user.check_password(form.password.data):
                    login_user(user)
                    # token = user.generate_token()
                    # session['token'] = token
                    return jsonify({
                        'code': 2000,
                        'msg': '访问成功',
                        # 'token': token,
                        'result': 'OK'
                    })
                else:
                    return jsonify({
                        'code': 3000,
                        'msg': '数据错误',
                        'result': '密码错误'
                    })
            else:
                return jsonify({
                    'code': 3001,
                    'msg': '数据库错误',
                    'result': '用户不存在'
                })
        else:
            return jsonify({
                'code': 3000,
                'msg': '数据错误',
                'result': '表单错误'
            })
