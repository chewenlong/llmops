#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/3 21:38
@Author  : chewl1
@File    : 1.RunnableParallel.py
"""
import os

import dotenv
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel

dotenv.load_dotenv()

if __name__ == '__main__':
    llm = ChatTongyi(
        model_name=os.getenv("MODEL"),
        dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
        top_p=0.8,
    )
    joke_prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话，尽可能短一些")
    poem_prompt = ChatPromptTemplate.from_template("请写一首关于{subject}的诗，尽可能短一些")

    parser = StrOutputParser()
    joke_chain = joke_prompt | llm | parser
    poem_chain = poem_prompt | llm | parser

    map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)
    # 两种写法都行
    # map_chain = RunnableParallel(
    #     {
    #         "joke_chain": joke_chain,
    #         "poem_chain": poem_chain,
    #     }
    # )
    result = map_chain.invoke(
        {
            "subject": "程序员"
        }
    )
    print("最终结果:", result)
