from src.agenticai.state.state import State


class ChatbotWithToolNode:
    def __init__(self, model, tools):
        self.llm = model
        self.tools = tools

    def process(self, state: State) -> dict:
        """
        Chatbot logic for processing the input state and generates a response with tool integration.
        """

        llm_with_tools = self.llm.bind_tools(self.tools)

        response = llm_with_tools.invoke(state["messages"])
        return {"messages": response}
