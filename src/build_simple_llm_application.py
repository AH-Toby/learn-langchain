#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   build_simple_llm_application.py
@Time    :   2024/11/21 19:22:15
@Author  :   Toby Wong 
@Version :   1.0
@Contact :   ahwt.ll@qq.com
@Desc    :   None
"""

import config
from langchain_community.chat_models import ChatZhipuAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

chat = ChatZhipuAI(
    model="glm-4",
    temperature=0.5,
)

messages = [
    AIMessage(content="Hi."),  # The first message is always an AI message
    SystemMessage(content="Your role is a poet."),  # The AI responds with a system message
    HumanMessage(content="Write a short poem about AI in four lines with chinese characters."),
]

response = chat.invoke(messages)
print(response.content)  # Displays the AI-generated poem
