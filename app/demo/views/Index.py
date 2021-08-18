#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/12 4:42 下午
# software: PyCharm
"""
文件说明：
"""
from flask_restful import Resource
from flask import request, redirect, url_for
from flask_login import login_required
from flask import session


class Index(Resource):
    # method_decorators = [login_required]
    def get(self):

        # if not request.cookies:
        #     # 如果没有cookie跳转到登录界面
        #     # return redirect(url_for('api.login'))
        #     return redirect(url_for('api.register', next=request.full_path))
        return '这个主页面'
