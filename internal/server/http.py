#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/10/29 21:47
@Author  : chewl1
@File    : http1.py
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config
from internal.exception.exception import CustomerException
from internal.model import App
from internal.router import Router
from pkg.response import json, Response, HttpCode


class Http(Flask):
    """http服务引擎"""

    def __init__(self, *args, conf: Config, db: SQLAlchemy, router: Router, **kwargs):
        super().__init__(*args, **kwargs)

        # 初始化应用配置
        self.config.from_object(conf)

        # 注册绑定异常错误处理
        self.register_error_handler(Exception, self._register_error_handler)

        # 初始化flask扩展
        db.init_app(self)

        with self.app_context():
            _ = App()
            db.create_all()

        # 注册应用路由
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        # 1.异常是不是我们自定义的异常，如果是可以提取message和code信息
        if isinstance(error, CustomerException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {}
            ))
        # 2.如果不是我们自定义的异常，则有可能是程序，数据库抛出的异常，也可以提取信息，设置为fail状态码
        print("环境", os.getenv("FLASK_ENV"))
        if os.getenv("FLASK_ENV") == "development":
            raise error
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data={}
            ))
