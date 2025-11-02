#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/2 17:12
@Author  : chewl1
@File    : 1.StrOutputParser使用技巧.py
"""
import os

import dotenv
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()

if __name__ == '__main__':
    parser = StrOutputParser()
    content = parser.parse("程序员的工厂")

    llm = ChatTongyi(
        model_name=os.getenv("MODEL"),
        dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
        top_p=0.8,
    )

    prompt = ChatPromptTemplate.from_template("{query}")
    contnt = parser.invoke(llm.invoke(prompt.invoke({"query": "你好，你是？"})))
    print(contnt)
