#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/2 11:27
@Author  : chewl1
@File    : 1prompt组件基础用法.py
"""
from datetime import datetime

from langchain_core.messages import AIMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder

if __name__ == '__main__':
    prompt = PromptTemplate.from_template("请讲一个关于{subject}的冷笑话。")
    print(prompt.format(subject="程序员"))
    print("================================")
    prompt_value = prompt.invoke({"subject": "程序员"})
    print(prompt_value)
    print(prompt_value.to_string())
    print(prompt_value.to_messages())
    print("================================")
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", "请根据用户的提问进行回复，当前时间为{now}"),
        MessagesPlaceholder("chat_history"),
        HumanMessagePromptTemplate.from_template("请讲一个关于{subject}的冷笑话。")
    ]
    ).partial(now=datetime.now())

    chat_prompt_value = chat_prompt.invoke({
        "subject": "程序员",
        "chat_history": [
            ("human", "我是慕小课"),
            AIMessage("你好，有什么可以帮到您")
        ]
    })
    print(chat_prompt_value)
    print(chat_prompt_value.to_string())
