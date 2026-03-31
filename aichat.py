import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

st.title("AI感情助手")
st.header("欢迎来到AI感情助手！")
# 加载环境变量
load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
)
# ai初始性格
AIChatName = "小A"
AIChatTrait = "小A是一个活泼的助手，能帮助主人解决各种问题。"

# 消息历史
if "messages" not in st.session_state:
    st.session_state.messages = []
#ai性格记忆化 
if "AIChatName" not in st.session_state:
    st.session_state.AIChatName = AIChatName
if "AIChatTrait" not in st.session_state:
    st.session_state.AIChatTrait = AIChatTrait

# 展示历史
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

with st.sidebar:
    st.subheader("人物配置")
    AINewName= st.text_input("人物名称", value=AIChatName)
    AINewTrait = st.text_area("自定义人物描述", value=AIChatTrait, height=300)

UserMessage = st.chat_input("主人请说")
if UserMessage:
    # 加入用户消息
    st.session_state.messages.append({"role": "user", "content": UserMessage})

    # 显示用户消息流式输出
    with st.chat_message("user"):
        ma = st.empty()
        s = ""
        for x in UserMessage:
            s += x
            ma.write(s)

    messages_to_send = [
        {"role": "system",
         "content": f"你的名字为{st.session_state.AIChatName}，你的性格是{st.session_state.AIChatTrait}"},  # 永远有内容
        *st.session_state.messages
    ]

    response = client.chat.completions.create(
        model=os.getenv("MODULE"),
        messages=messages_to_send,
        stream=True
    )

    # 流式显示回复
    res = st.empty()
    ai_resp = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            ai_resp += chunk.choices[0].delta.content
            res.chat_message("assistant").markdown(ai_resp)

    st.session_state.messages.append({"role": "assistant", "content": ai_resp})
