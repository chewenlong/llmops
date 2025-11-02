#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/11/2 20:30
@Author  : chewl1
@File    : 2.JsonOutputParser使用技巧.py
"""
import os

import dotenv
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

dotenv.load_dotenv()


class Joke(BaseModel):
    joke: str = Field(description="回答用户的冷笑话")
    punchline: str = Field(description="冷笑话的笑点")


if __name__ == '__main__':
    llm = ChatTongyi(
        model_name=os.getenv("MODEL"),
        dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
        top_p=0.8,
    )

    paser = JsonOutputParser(pydantic_object=Joke)
    prompt = ChatPromptTemplate.from_template("请根据用户提问进行回答。\n{format_instructions}\n{query}").partial(
        format_instructions=paser.get_format_instructions()
    )

    resp = paser.invoke(llm.invoke(prompt.invoke({"query": "讲一个关于程序员的冷笑话"})))
    print(resp)
