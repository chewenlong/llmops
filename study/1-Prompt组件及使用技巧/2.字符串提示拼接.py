#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/2 12:06
@Author  : chewl1
@File    : 2.字符串提示拼接.py
"""
from langchain_core.prompts import PromptTemplate

if __name__ == '__main__':
    prompt = (
            PromptTemplate.from_template("请讲一个关于{subject}的冷笑话。")
            + "让我开心下"
            + "\n使用{languge}语言"
    )
    print(prompt.invoke({"subject": "程序员", "languge": "中文"}))
