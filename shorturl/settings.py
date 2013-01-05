#!/usr/bin/env python
# -*- coding: utf-8 -*-

DEBUG = True  # 调试模式
TEMPLATE_DIR = 'templates/'  # 模板目录
BASE_TEMPLATE = 'base'  # 基础模板

# URL 映射
URLS = (
    '/', 'Index',
    '(/j)?/shorten', 'Shorten',
    '/([0-9a-zA-Z]{5,})', 'Expand',
    '/j/expand', 'Expand',
    '/.*', 'Index',
)

# 数据库配置
DATABASES = {
    'dbn': 'mysql',
    'db': 'shorturl',
    'user': 'py',
    'pw': 'py_passwd',
    'host': 'localhost',
    'port': 3306,
}
