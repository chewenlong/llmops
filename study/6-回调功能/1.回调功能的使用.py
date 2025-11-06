#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/3 22:29
@Author  : chewl1
@File    : 1.回调功能的使用.py
"""

import os
import time
from typing import Any
from uuid import UUID

from langchain_community.chat_models import ChatTongyi
from langchain_core.callbacks import StdOutCallbackHandler, BaseCallbackHandler
from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough


class LLMOpsCallbackHandler(BaseCallbackHandler):
    """自定义回调处理器"""
    start: float = 0

    def on_chat_model_start(
            self,
            serialized: dict[str, Any],
            messages: list[list[BaseMessage]],
            *,
            run_id: UUID,
            parent_run_id: UUID | None = None,
            tags: list[str] | None = None,
            metadata: dict[str, Any] | None = None,
            **kwargs: Any,
    ) -> Any:
        print("聊天模型开始执行了")
        print("serialized:", serialized)
        print("messages:", messages)
        self.start = time.time()

    def on_llm_end(
            self,
            response: dict[str, Any],
            *,
            run_id: UUID,
            parent_run_id: UUID | None = None,
            tags: list[str] | None = None,
            metadata: dict[str, Any] | None = None,
            **kwargs: Any,
    ) -> Any:
        end: float = time.time()
        print(f"LLM 执行结束，耗时：{end - self.start}")


if __name__ == '__main__':
    prompt = ChatPromptTemplate.from_template("{query}")
    llm = ChatTongyi(
        model_name=os.getenv("MODEL"),
        dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
        top_p=0.8,
    )
    parser = StrOutputParser()

    chain = {"query": RunnablePassthrough()} | prompt | llm | parser
    result = chain.invoke("你好，你是？", config={"callbacks": [StdOutCallbackHandler(), LLMOpsCallbackHandler()]})
    print("最终结果:", result)
