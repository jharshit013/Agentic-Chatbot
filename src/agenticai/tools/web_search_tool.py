from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


def get_tools():
    """
    Returns a list of tools to be used in the chatbot.
    """

    tools = [TavilySearchResults(max_results=2)]
    return tools


def create_tool_node(tools):
    """
    Creates a tool node from the provided tools.
    This function initializes a ToolNode with the given tools.
    """

    tool_node = ToolNode(tools=tools)
    return tool_node
