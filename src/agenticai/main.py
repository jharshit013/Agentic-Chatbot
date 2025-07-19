import streamlit as st
from src.agenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.agenticai.LLMS.groqllm import GroqLLM
from src.agenticai.graph.graph_builder import GraphBuilder
from src.agenticai.ui.streamlitui.display_result import DisplayResultStreamlit


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

    if user_message:
        try:
            object_llm_config = GroqLLM(user_controls_input=user_input)
            model = object_llm_config.get_llm_model()

            if not model:
                st.error("Error: Failed to initialize the LLM model.")
                return

            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: No Use Case selected.")
                return

            graph_builder = GraphBuilder(model)

            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(
                    usecase, graph, user_message
                ).display_result_on_ui()

            except Exception as e:
                st.error(f"Error: Error setting up the graph - {e}")
                return

        except Exception as e:
            st.error(f"An error occurred: {e}")
            return
