#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/8 12:20 下午
# software: PyCharm
"""
文件说明：执行文件
"""

import sys
import os

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))


# 增加导包路径
sys.path.insert(0, os.path.join(BASE_DIR, 'framework'))
from config.setting_dev import DefaultConfig
from flask import jsonify
from framework import create_app

app = create_app(DefaultConfig)


@app.route('/')
def route_map():
    app.logger.info('hello_log')
    rules_iterator = app.url_map.iter_rules()
    return jsonify({
        rule.endpoint: rule.rule for rule in rules_iterator if rule.endpoint not in ('route_map', 'static')
    })


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG_MODEL_SWITCH'], host=app.config['HOST'], port=app.config["PORT"])

