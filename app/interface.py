import streamlit as st
from app.utils import initialize_session_state

def display_chat(messages):
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def get_user_input():
    return st.chat_input("quem vem virando a esquina?")

def add_message(role: str, content: str):
    import streamlit as st
    st.chat_message(role).markdown(content)
    st.session_state.messages.append({"role": role, "content": content})
