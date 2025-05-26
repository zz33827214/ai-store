import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="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")

st.title("🏍️ AI 摩托車配件客服")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "你是摩托車配件網站的客服"}
    ]

user_input = st.text_input("請輸入您的問題：")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

    st.markdown(f"**AI客服：** {reply}")
