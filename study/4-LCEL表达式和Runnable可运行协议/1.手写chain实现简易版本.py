#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/2 22:23
@Author  : chewl1
@File    : 1.手写chain实现简易版本.py
"""
import os
from typing import Any

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


class Chain:
    steps: list = []

    def __init__(self, steps: list):
        self.steps = steps

    def invoke(self, input: Any) -> Any:
        for step in self.steps:
            input = step.invoke(input)
            print("步骤:", step)
            print("输出:", input)
            print("=================")
        return input


if __name__ == '__main__':
    chain = Chain(steps=[prompt, llm, parser])
    result = chain.invoke({"query": "讲一个程序员冷笑话"})
    print("最终结果:", result)
