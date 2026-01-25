from dotenv import load_dotenv
import os

# LangChain message and prompt utilities
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Google Gemini LLM wrapper for LangChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Tool and agent helpers
from langchain.tools import tool
from langchain.agents import create_openai_tools_agent, AgentExecutor

# Todoist Python SDK
from todoist_api_python.api import TodoistAPI


# -------------------- ENV SETUP --------------------
# Load environment variables from .env file
load_dotenv()

todoist_api_token = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize Todoist client
todoist = TodoistAPI(todoist_api_token)


# -------------------- TOOLS --------------------
@tool
def add_task(task, desc=None):
    """
    Add a new task to the user's Todoist list.

    Args:
        task (str): Task title.
        desc (str, optional): Task description.
    """
    todoist.add_task(content=task, description=desc)


@tool
def show_tasks():
    """
    Fetch and return all tasks from Todoist.

    Returns:
        list: List of task names.
    """
    result_paginator = todoist.get_tasks()
    tasks = []

    # Todoist returns paginated results
    for task_list in result_paginator:
        for task in task_list:
            tasks.append(task.content)

    return tasks


# Register tools
tools = [add_task, show_tasks]


# -------------------- LLM SETUP --------------------
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=gemini_api_key,
    temperature=0.3
)


# -------------------- PROMPT --------------------
system_prompt = """You are a helpful assistant.
You will help the user add tasks.
You will help the user show existing tasks.

If the user asks to show the tasks (for example, "show me the tasks"),
print them in a bullet list format.
"""


# Build structured prompt template with memory placeholders
prompt = ChatPromptTemplate([
    ("system", system_prompt),
    MessagesPlaceholder("history"),           # Conversation memory
    ("user", "{input}"),                      # User input slot
    MessagesPlaceholder("agent_scratchpad")   # Agent reasoning workspace
])


# -------------------- AGENT SETUP --------------------
agent = create_openai_tools_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=False
)


# -------------------- CHAT LOOP --------------------
history = []

while True:
    # Read user input from CLI
    user_input = input("You: ")

    # Run agent with memory
    response = agent_executor.invoke({
        "input": user_input,
        "history": history
    })

    # Print assistant output
    print(response["output"])

    # Store conversation history
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response["output"]))