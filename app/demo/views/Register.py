#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/12 3:43 下午
# software: PyCharm
"""
文件说明：
"""
from flask_restful import Resource
from flask import request, jsonify, current_app
from framework.utils.forms import RegisterForm
from app.demo.models.User import User, db
from flask_restful.reqparse import RequestParser

class Register(Resource):
    """注册视图"""
    def post(self):
        form = RegisterForm()
        json_parser = RequestParser()
        args = json_parser.parse_args()
        # json_parser.add_argument('mobile', type=parser.mob)
        if form.validate_on_submit():
            try:
                user = User()

                # user_args = {
                #     'name': form.username.data,
                #     'password': form.password.data,
                #     # 'Email': form.Email.data
                # }
                #
                # user.__dict__.update(user_args)
                # 此方法无法激活密码加密
                user.name = form.username.data
                user.password = form.password.data
                db.session.add(user)
                db.session.commit()
            except Exception as e:
                return jsonify({
                    'code': 3001,
                    'msg': '数据库错误',
                    'result': e.args[0]
                })
        else:
            return jsonify({
                'code': 3000,
                'msg': '数据错误',
                'result': form.errors
            })
        return jsonify({
            'code': 2000,
            'msg': '访问成功',
            'result': 'ok'
        })
        pass
