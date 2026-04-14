import streamlit as st

def get_memory():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    return st.session_state.chat_history

def update_memory(user, bot):
    st.session_state.chat_history.append({
        "user": user,
        "bot": bot
    })