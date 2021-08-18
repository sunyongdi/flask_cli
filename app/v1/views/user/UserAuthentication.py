#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/18 7:13 下午
# software: PyCharm
"""
文件说明：
"""
from flask_restful import Resource
from flask import request, current_app
from app.v1.models.User import User
from app.v1.models import db
from framework.utils.RespUtil import RespUtil

class UserAuthentication(Resource):
    """
    param: mobile 手机号
    param: code 验证码
    注册并登录
    return: token
    """
    def post(self):
        mobile = request.form.get('mobile')
        code = request.form.get('code')
        if code == current_app.redis_pool.get(f'app:code:{mobile}') or 1:
            # TODO 生产环境将or 1去掉
            # 短信验证通过
            user = User.query.filter_by(mobile=mobile).first()  # 是否是注册用户
            if user is None:
                try:
                    user = User(mobile=mobile, name=mobile)
                    db.session.add(user)
                    db.session.commit()
                except Exception as e:
                    current_app.logger.exception(e)
                    print(e.args)
                    # return {
                    #     'code': 3000,
                    #     'msg': '数据错误'
                    # }
                    return RespUtil.data_error('数据库错误')
            # 注册登录/登录
            # return {
            #     'code': 2000,
            #     'msg': '访问成功',
            #     # 'token': ''
            # }
            # return RespUtil.ok('登录成功')
            return RespUtil.ok({
                'token': 'asdasdasd'
            })

        else:
            # return {
            #     'code': 3001,
            #     'msg': '用户或验证码错误'
            # }
            return RespUtil.data_error('用户或验证码错误')
