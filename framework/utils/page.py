#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/12 4:36 下午
# software: PyCharm
"""
文件说明：页面的功能工具
后期加入验证url
"""

from flask import request, redirect, url_for
from urllib.parse import urlparse, urljoin


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

def redirect_back(defaule='api.register', **kwargs):
    '''
    页面跳转上一个页面，没有默认回到注册页面
    '''
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)

    return redirect(url_for(defaule, **kwargs))
