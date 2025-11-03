#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/2 22:29
@Author  : chewl1
@File    : 2.LCEL表达式简化版本.py
"""
import os

from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatTongyi(
    model_name=os.getenv("MODEL"),
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
    top_p=0.8,
)
parser = StrOutputParser()

if __name__ == '__main__':
    chain = prompt | llm | parser
    result = chain.invoke({"query": "讲一个程序员冷笑话"})
    print("最终结果:", result)
