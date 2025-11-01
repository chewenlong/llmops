#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/10/31 22:01
@Author  : chewl1
@File    : default_config.py
"""
# 应用默认配置项目
DEFAULT_CONFIG = {
    # WTF CSRF 保护
    "WTF_CSRF_ENABLED": "False",
    
    # SQLAlchemy 配置
    "SQLALCHEMY_DATABASE_URI": "",
    "SQLALCHEMY_POOL_SIZE": 30,
    "SQLALCHEMY_POOL_RECYCLE": 3600,
    "SQLALCHEMY_ECHO": "True"
}
