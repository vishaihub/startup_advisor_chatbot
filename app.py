import streamlit as st
from prompts.startup_prompt import build_prompt
from services.gemini_service import get_gemini_response
from memory.session_memory import get_memory, update_memory
from logger import setup_logger

setup_logger()

st.set_page_config(page_title="Startup Advisor Chatbot", layout="centered")

st.title("🚀 Startup Advisor Chatbot")

history = get_memory()

# Display chat history
for chat in history:
    st.chat_message("user").write(chat["user"])
    st.chat_message("assistant").write(chat["bot"])

user_input = st.chat_input("Let's discuss your startup idea...")

if user_input:
    st.chat_message("user").write(user_input)

    with st.spinner("Thinking..."):
        prompt = build_prompt(user_input, history)
        response = get_gemini_response(prompt)

    st.chat_message("assistant").write(response)

    update_memory(user_input, response)