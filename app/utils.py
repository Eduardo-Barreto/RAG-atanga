def initialize_session_state(key: str, default_value):
    import streamlit as st
    if key not in st.session_state:
        st.session_state[key] = default_value
