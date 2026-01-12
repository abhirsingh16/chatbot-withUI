from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
from typing import TypedDict, Annotated
from dotenv import load_dotenv
import sqlite3


load_dotenv()

llm = ChatGroq(
    model = "llama-3.1-8b-instant"
)



class ChatState(TypedDict):

    messages : Annotated[list[BaseMessage], add_messages]



def chat_node(state: ChatState):

    messages = state['messages']

    response = llm.invoke(messages)

    return {"messages":response}


graph = StateGraph(ChatState)


graph.add_node("chat_node", chat_node)

graph.add_edge(START,"chat_node")
graph.add_edge("chat_node", END)

# creating database
conn = sqlite3.connect(database = "chatbot.db", check_same_thread=False)

checkpointer = SqliteSaver(conn = conn)


chatbot = graph.compile(checkpointer=checkpointer)

# checkpointer.list(None)

def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config["configurable"]["thread_id"])

    return list(all_threads)