#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/1 15:41
@Author  : chewl1
@File    : sqlalchemy.py
"""
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):
    """重写 SQLAlchemy 类以实现自动提交"""

    @contextmanager
    def auto_commit(self):
        """自动提交上下文管理器"""
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
