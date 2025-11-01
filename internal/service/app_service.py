#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/1 13:16
@Author  : chewl1
@File    : app_service.py
"""
import uuid
from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy
from injector import inject

from internal.model import App


@inject
@dataclass
class AppService:
    """应用服务逻辑"""
    db: SQLAlchemy

    def create_app(self) -> App:
        app = App(name="测试机器人", account_id=uuid.uuid4(), icon="", description="这是一个智能机器人应用")
        self.db.session.add(app)
        self.db.session.commit()
        return app

    # select by id
    def get_app_by_id(self, app_id: uuid.UUID) -> App:
        app = self.db.session.query(App).get(app_id)
        return app

    # update by id
    def update_app(self, app_id: uuid.UUID) -> App:
        app = self.get_app_by_id(app_id)
        app.name = "聊天机器人"
        self.db.session.commit()
        return app

    # delete by id
    def delete_app(self, app_id: uuid.UUID) -> None:
        app = self.get_app_by_id(app_id)
        self.db.session.delete(app)
        self.db.session.commit()
        return app
