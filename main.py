from app.engine import QueryEngine
from app.interface import display_chat, get_user_input, add_message
from app.utils import initialize_session_state
import streamlit as st

st.title("RAG atanga ele curte ele dança")

initialize_session_state("messages", [])
query_engine = QueryEngine()

display_chat(st.session_state.messages)

if prompt := get_user_input():
    add_message("user", prompt)

    try:
        response = query_engine.query(prompt)
        add_message("assistant", response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
