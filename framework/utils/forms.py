#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/9 9:32 上午
# software: PyCharm
"""
文件说明：
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, Form
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email
from flask import request

# 自定义表单
def is_syd(message=None):
    if message is None:
        return "Must be 42"

    def _is_syd(form, field):
        if field.data != 'syd':
            raise ValidationError(message)

    return _is_syd


class BaseForm(FlaskForm):
    class Meta:
        locales = ['zh']


#
# class MyForm(BaseForm):
#
#
#     name = StringField('Name', validators=[DataRequired(), Length(1, 5, message='至少5位')])


class RegisterForm(BaseForm):
    # TODO 邮箱、手机、地址等验证信息
    # username = StringField(validators=[DataRequired(message='用户名格式错误'), is_syd(message='表单验证的用户名必须是syd')])
    username = StringField(validators=[DataRequired(message='用户名格式错误')])
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入您的密码'), Length(6, 12, message='密码长度6-12位')])
    password1 = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入您的密码'), Length(6, 12, message='密码长度6-12位'),
        EqualTo('password', message='两次密码不一致')
    ])
    #
    # Email = StringField(validators=[Email(message='格式错误')])

class LoginForm(BaseForm):
    # username = StringField(validators=[DataRequired(message='用户名格式错误'), is_syd(message='表单验证的用户名必须是syd')])
    username = StringField(validators=[DataRequired(message='用户名格式错误')])
    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入您的密码'), Length(6, 12, message='密码长度6-12位')])
    # password1 = PasswordField(validators=[
    #     DataRequired(message='密码不可以为空，请输入您的密码'), Length(6, 12, message='密码长度6-12位'),
    #     EqualTo('password', message='两次密码不一致')
    # ])