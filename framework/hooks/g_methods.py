#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/12 11:37 上午
# software: PyCharm
"""
文件说明：
"""
from flask import g, request
import json
from flask_restful.reqparse import RequestParser


def get_name():
    g.name = request.args.get('user')


def validate_token():
    """
    将登录和注册接口暴露在外，其他要求验证token
    提交数据的方式
    1、request.form
    2、request.args
    3、request.
    """
    # if request.path not in ['/api/login', 'api/register']:
    #     pass
    #     data = None
    #     if request.method == 'POST':
    #         data = request.form
    #     if not data:
    #         data_json = request.args.get('json')
    #         if data_json is not None:
    #             data = json.loads(data_json)
    #         else:
    #             data = request.args
    #     param = dict(data)
    #     token = param.get('token')
    pass
