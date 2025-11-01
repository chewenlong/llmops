#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/10/30 22:32
@Author  : chewl1
@File    : exception.py
"""
from dataclasses import field
from typing import Any

from pkg.response import HttpCode


class CustomerException(Exception):
    """基础自定义异常信息"""
    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = "", data: Any = None):
        super().__init__()
        self.message = message
        self.data = data


class FailException(CustomerException):
    """基础失败异常信息"""
    pass


class NotFoundException(CustomerException):
    """资源未找到异常信息"""
    code = HttpCode.NOT_FOUND


class UnthorizedException(CustomerException):
    """未授权访问异常信息"""
    code = HttpCode.UNAUTHORIZED


class ForbiddenException(CustomerException):
    """禁止访问异常信息"""
    code = HttpCode.FORBIDDEN


class ValidateErrorException(CustomerException):
    """参数校验错误异常信息"""
    code = HttpCode.VALIDATE_ERROR
