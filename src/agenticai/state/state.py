from typing_extensions import TypedDict, list
from typing import Annotated
from langgraph.graph.message import add_messages


class State(TypedDict):
    """
    Represents the structure of the state used in the graph.
    """

    message: Annotated[list, add_messages]  # List of messages in the conversation
