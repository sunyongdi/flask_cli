#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/12 10:03 上午
# software: PyCharm
"""
文件说明：
"""

from flask_restful import Resource
from flask import request, make_response, session, g


class Demo1(Resource):
    def get(self):
        name = g.name
        return 'he'
        if 'logged_in' in session:
            return "😄"
        # get 请求的params中的数据
        args = request.args
        # 当前的蓝图名称
        blueprint = request.blueprint
        cookies = request.cookies
        data = request.data
        endpoint = request.endpoint
        files = request.files
        form = request.form
        values = request.values
        get_data = request.get_data()
        get_json = request.get_json()
        headers = request.headers
        js_json = request.is_json
        json = request.json
        method = request.method
        referrer = request.referrer
        scheme = request.scheme
        user_agent = request.user_agent
        return f'request:{args, blueprint, cookies, data, endpoint, form, files, values, get_data, get_json, headers, json, js_json, method, referrer, scheme, user_agent}'

    def post(self):
        # get 请求的params中的数据
        args = request.args
        # 当前的蓝图名称
        blueprint = request.blueprint
        cookies = request.cookies
        data = request.data
        endpoint = request.endpoint
        files = request.files
        form = request.form
        values = request.values
        get_data = request.get_data()
        get_json = request.get_json()
        headers = request.headers
        js_json = request.is_json
        json = request.json
        method = request.method
        referrer = request.referrer
        scheme = request.scheme
        user_agent = request.user_agent
        return f'request:{args, blueprint, cookies, data, endpoint, form, files, values, get_data, get_json, headers, json, js_json, method, referrer, scheme, user_agent}'


