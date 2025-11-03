#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/3 21:38
@Author  : chewl1
@File    : 1.RunnableParallel.py
"""
import os
from operator import itemgetter

import dotenv
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()


def retrieval(query: str) -> str:
    # 模拟检索上下文
    print("正在检索")
    return "我是慕小课。"


if __name__ == '__main__':
    llm = ChatTongyi(
        model_name=os.getenv("MODEL"),
        dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
        top_p=0.8,
    )
    prompt = ChatPromptTemplate.from_template("""请根据用户的问题回答，可以参考对应的上下文进行回答。
        <context>
            {context}
        </context>
        用户的提问是{query}
        """)
    parser = StrOutputParser()
    parallel_chain = {
        "context": lambda x: retrieval(x["query"]),
        "query": itemgetter("query")
    }
    # 下面这样也行，因为|会自动将前面的转为Runnable类型
    # parallel_chain = RunnableParallel({
    #     "context": lambda x: retrieval(x["query"]),
    #     "query": itemgetter("query")
    # })
    chain = parallel_chain | prompt | llm | parser
    resp = chain.invoke({"query": "你好，我是谁"})
    print(resp)
