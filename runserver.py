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

# 查看文件路径
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname((os.path.abspath(__file__)))

# print(os.path.abspath(__file__))
# print(BASE_DIR)
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 增加导包路径
sys.path.insert(0, os.path.join(BASE_DIR, 'framework'))
# print(sys.path)
from config.setting import DefaultConfig
from flask import jsonify
from framework import create_app

app = create_app(DefaultConfig)


@app.route('/')
def route_map():
    rules_iterator = app.url_map.iter_rules()
    return jsonify({
        rule.endpoint: rule.rule for rule in rules_iterator if rule.endpoint not in ('route_map', 'static')
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)

# if __name__ == '__main__':
# print(sys.path)
# print(app.config)
# app.run(host='0.0.0.0', port=9090, debug=True)
