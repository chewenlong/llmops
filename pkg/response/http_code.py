#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/10/30 21:51
@Author  : chewl1
@File    : http_code.py
"""
from enum import Enum


class HttpCode(str, Enum):
    """HTTP基础业务状态码枚举类"""

    SUCCESS = "success"  # 请求成功
    FAIL = "fail"
    UNAUTHORIZED = "unauthorized"  # 未授权访问
    FORBIDDEN = "forbidden"  # 禁止访问
    VALIDATE_ERROR = "validate_error"  # 参数校验错误
    NOT_FOUND = "not_found"  # 资源未找到
