import streamlit as st

st.title("ai感情助手")
st.header("欢迎来到ai感情助手！")
st.write("在这里，你可以与AI进行情感交流，分享你的心情和感受。无论你是开心、难过、焦虑还是兴奋，AI都会倾听你的心声，并给予你温暖的回应。")
st.write("请在下面的输入框中分享你的心情，AI会尽力理解并给予你支持和建议。无论你需要一个倾听者，还是想要一些建议，AI都会在这里陪伴你。")
st.write("记住，你并不孤单，AI会一直在这里陪伴你，帮助你度过每一个情感的时刻。")


usermessage =  st.chat_input("你好，不知道你有什么困难，在这ai会帮助你(ai develop everything)")
if usermessage:
    st.chat_message("user").write(usermessage)
