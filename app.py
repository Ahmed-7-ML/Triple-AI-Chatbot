import streamlit as st
from chatbot import chat

st.set_page_config(
    page_title="Triple AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Triple AI Chatbot")
st.caption("Powered by LangChain")

# ---> Session State <---
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---> Display Chat History <---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---> User Input <---
user_input = st.chat_input("Ask me something...")
domain = st.text_input("Interested Topic", value="Machine Learning")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # answer, confidence = chat(user_input=user_input, domain=domain)
            answer = chat(user_input=user_input, domain=domain)
            st.markdown(answer)
            # st.caption(f"🧠 Confidence: **{confidence.capitalize()}**")
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
