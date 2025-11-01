#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/10/29 21:22
@Author  : chewl1
@File    : router.py
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    """路由控制器"""
    app_handler: AppHandler

    def register_router(self, app: Flask):
        """注册路由"""
        # 创建一个蓝图
        bp = Blueprint('llmops', __name__, url_prefix="")
        # 将url与控制器方法做绑定
        bp.add_url_rule('/ping', view_func=self.app_handler.ping)
        bp.add_url_rule("/http/completion", view_func=self.app_handler.completion, methods=["POST"])
        bp.add_url_rule("/app/create", view_func=self.app_handler.create_app, methods=["POST"])
        bp.add_url_rule("/app/<uuid:id>", view_func=self.app_handler.get_app, methods=["GET"])
        bp.add_url_rule("/app/<uuid:id>", view_func=self.app_handler.update_app, methods=["PUT"])
        bp.add_url_rule("/app/<uuid:id>", view_func=self.app_handler.delete_app, methods=["DELETE"])
        app.register_blueprint(bp)
