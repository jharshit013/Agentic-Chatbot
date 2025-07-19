from langgraph.graph import StateGraph, START, END
from src.agenticai.state.state import State
from src.agenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.agenticai.tools.web_search_tool import get_tools, create_tool_node
from langgraph.prebuilt import tools_condition
from src.agenticai.nodes.chatbot_with_tools_node import ChatbotWithToolNode


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This metthod initializes the chatbot node using `BasicChatbotNode` class and integrates it into the graph.
        This chatbot node is set as both entry and exit point of the graph.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node
        and a tool node. It defines tools, initializes the chatbot with tool
        capabilities, and sets up conditional and direct edges between nodes.
        The chatbot node is set as the entry point.
        """

        tools = get_tools()
        tool_node = create_tool_node(tools)

        self.chatbot_with_tools_node = ChatbotWithToolNode(self.llm, tools)

        self.graph_builder.add_node("chatbot", self.chatbot_with_tools_node.process)
        self.graph_builder.add_node("tools", tool_node)

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase: str):
        """Sets up the graph for the selected usecase"""
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        if usecase == "Chatbot 2.0":
            self.chatbot_with_tools_build_graph()

        return self.graph_builder.compile()
