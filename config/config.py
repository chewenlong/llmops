#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/10/30 21:31
@Author  : chewl1
@File    : config.py
"""
import os
from typing import Any

from config.default_config import DEFAULT_CONFIG


def _get_env(key: str) -> Any:
    """获取环境变量的值，找不到则返回默认值"""
    return os.getenv(key, DEFAULT_CONFIG.get(key))


def _get_bool_env(key: str) -> bool:
    """获取布尔类型的环境变量值"""
    value: str = _get_env(key)
    return value.lower() == 'true' if value is not None else False


class Config:
    """应用配置类"""

    def __init__(self):
        # 关闭 CSRF 保护
        self.WTF_CSRF_ENABLED = _get_bool_env("WTF_CSRF_ENABLED")

        # 数据库配置
        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            'pool_size': int(_get_env("SQLALCHEMY_POOL_SIZE")),
            'pool_recycle': int(_get_env("SQLALCHEMY_POOL_RECYCLE")),
        }
        self.SQLALCHEMY_ECHO = _get_env("SQLALCHEMY_ECHO")
