#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/2 12:13
@Author  : chewl1
@File    : 3消息提示模板拼接.py
"""
from langchain_core.prompts import ChatPromptTemplate

if __name__ == '__main__':
    sys_chat_prompt = ChatPromptTemplate.from_messages([
        ("system", "请根据用户的提问进行回复，我叫{username}")
    ])

    human_chat_prompt = ChatPromptTemplate.from_messages([
        ("human", "{query}")
    ])

    chat_prompt = sys_chat_prompt + human_chat_prompt
    print(chat_prompt)
    print("================================")
    print(chat_prompt.invoke(
        {
            "username": "慕小课",
            "query": "你是谁？"
        }
    ))
