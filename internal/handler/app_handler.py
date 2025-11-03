#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/10/29 21:19
@Author  : chewl1
@File    : app_handler.py.py
"""
import os
import uuid
from dataclasses import dataclass

from injector import inject
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from internal.service import AppService
from pkg.response import success_json, validate_error_json, success_message


@inject
@dataclass
class AppHandler:
    """应用控制器"""
    app_service: AppService

    def create_app(self):
        """调用服务创建新的APP记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已创建成功，id为{app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app_by_id(id)
        return success_message(f"应用已查询成功，名称为{app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已更新成功，名称为{app.name}")

    # delete by id
    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用已删除成功，名称为{app.name}")

    def completion(self):
        """聊天接口"""
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)
        prompt = ChatPromptTemplate.from_template("{query}")
        llm = ChatTongyi(
            model_name=os.getenv("MODEL"),
            dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
            top_p=0.8,
        )
        parser = StrOutputParser()
        chain = prompt | llm | parser
        ai_message = chain.invoke({"query": req.query.data})
        content = parser.invoke(ai_message)
        resp = success_json(data={"content": content})
        return resp

    def ping(self):
        raise FailException("数据未找到")
        # return {"ping": "tong"}
