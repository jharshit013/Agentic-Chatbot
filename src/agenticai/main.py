import streamlit as st
from src.agenticai.ui.streamlitui.loadui import LoadStreamlitUI


def load_agenticai_app():
    """
    Load the Agentic AI application using Streamlit UI.
    """

    load_ui = LoadStreamlitUI()
    user_input = load_ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    user_message = st.chat_input("Enter your message:")
