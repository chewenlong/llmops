#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/2 16:02
@Author  : chewl1
@File    : 1.llm与ChatModel使用技巧.py
"""
import os
from datetime import datetime

import dotenv
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()
if __name__ == '__main__':
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一个有帮助的助手,现在的时间是{now}"),
            ("human", "{query}")
        ]
    ).partial(now=datetime.now())

    llm = ChatTongyi(
        model_name=os.getenv("MODEL"),
        dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
        top_p=0.8,
    )

    resp_msg = llm.invoke(prompt.invoke({"query": "现在是几点，讲一个程序员冷笑话"}))
    print(resp_msg.content)
    print(resp_msg.type)
    print(resp_msg.response_metadata)
