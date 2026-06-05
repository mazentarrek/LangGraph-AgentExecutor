# This file will contain the implementation of our LangGraph nodes 

from dotenv import load_dotenv
# A simple object that has the dictionary of the key messages that will keep track of all messages between 
# human message and Ai message
from langgraph.graph import MessagesState
# A node which will execute tools by checking the last message and if it has value of tool call it will 
# execute the tool call
from langgraph.prebuilt import ToolNode

from react import llm, tools

load_dotenv()

SYSTEM_MESSAGE = """
    You are a helpful assistant with access to tools to answer questions
"""

def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """
        Run the agent reasoning node
    """
    response = llm.invoke([{"role": "system", "content": SYSTEM_MESSAGE}, *state["messages"]])
    return {"messages": [response]}


tool_node = ToolNode(tools)
