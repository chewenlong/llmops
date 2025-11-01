#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/10/30 21:25
@Author  : chewl1
@File    : app_schema.py
"""
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """基础聊天接口请求验证"""
    query = StringField("query", validators=[
        DataRequired(message="用户的提问是必填的"),
        Length(max=2000, message="用户的提问长度不能超过2000个字符")
    ])
