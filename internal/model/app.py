#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/1 9:25
@Author  : chewl1
@File    : app.py
"""
import uuid
from datetime import datetime

from sqlalchemy import (
    UUID,
    DateTime,
    String,
    Text, PrimaryKeyConstraint, Index
)

from internal.extension.database_extension import db


class App(db.Model):
    """AI应用基础模型类"""
    __tablename__ = "app"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_app_id"),
        Index("idx_app_account_id", "account_id"),)

    id = db.Column(UUID, default=uuid.uuid4(), nullable=False, primary_key=True)
    account_id = db.Column(UUID, nullable=False)
    name = db.Column(String(255), nullable=False, default="")
    icon = db.Column(String(255), nullable=False, default="")
    description = db.Column(Text, nullable=False, default="")
    status = db.Column(Text, nullable=False, default="")
    created_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    updated_at = db.Column(DateTime, default=datetime.now, nullable=False)
