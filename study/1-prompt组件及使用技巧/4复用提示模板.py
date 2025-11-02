from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

if __name__ == "__main__":
    # 定义各个子模板
    instruction_prompt = PromptTemplate.from_template("你正在模拟{persion}")
    example_prompt = PromptTemplate.from_template("""下面是一个交互例子：
        Q：{example_q}
        A：{example_a}
    """)
    start_prompt = PromptTemplate.from_template("""现在你是一个真实的人，请回答用户问题：
        Q：{input}
        A：
    """)

    # 直接组合成一个 ChatPromptTemplate
    prompt = ChatPromptTemplate.from_messages([
        ("system", instruction_prompt.template),
        ("user", example_prompt.template),
        ("user", start_prompt.template),
    ])

    print(prompt.invoke(
        {"persion": "小明", "example_q": "你喜欢什么？", "example_a": "我喜欢学习。", "input": "今天天气怎么样？"}))
    print()
    print(prompt.format(
        persion="小明",
        example_q="你喜欢什么？",
        example_a="我喜欢学习。",
        input="今天天气怎么样？"
    ))
