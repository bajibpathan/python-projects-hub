from dotenv import load_dotenv
import os
import gradio as gr

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI


# -------------------- ENV SETUP --------------------
# Load environment variables from .env file
load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

if not gemini_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")


# -------------------- SYSTEM PROMPT --------------------
system_prompt = """
You are Albert Einstein.

You answer with deep reasoning and curiosity.
You speak from Einstein's personal point of view and often share life experiences,
thought processes, and reflections along with explanations.

When asked about science, include both the theory and your personal journey with it.
"""


# -------------------- LLM SETUP --------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_key,
    temperature=0.5
)


# -------------------- PROMPT TEMPLATE --------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{input}")
])


# -------------------- CHAIN --------------------
# Pipeline: Prompt -> Gemini -> String Output
chain = prompt | llm | StrOutputParser()


# -------------------- CHAT HANDLER --------------------
def chat(user_input, history):
    """
    Handles each user interaction:
    - Converts Gradio history into LangChain messages
    - Invokes the chain
    - Updates chat history
    """

    langchain_history = []

    for item in history:
        if item["role"] == "user":
            langchain_history.append(HumanMessage(content=item["content"]))
        elif item["role"] == "assistant":
            langchain_history.append(AIMessage(content=item["content"]))

    # Invoke the LangChain pipeline
    response = chain.invoke({
        "input": user_input,
        "history": langchain_history
    })

    # Update UI history
    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": response})

    return "", history


def clear_chat():
    """Clears the chat history."""
    return "", []


# -------------------- UI --------------------
page = gr.Blocks(title="Chat with Einstein")

with page:
    gr.Markdown(
        """
        # 🧠 Chat with Albert Einstein  
        Ask questions and receive thoughtful, personal responses from Einstein himself.
        """
    )

    chatbot = gr.Chatbot(
        avatar_images=[None, "einstein.png"],
        show_label=False
    )

    msg = gr.Textbox(
        show_label=False,
        placeholder="Ask Einstein anything..."
    )

    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    clear = gr.Button("Clear Chat")
    clear.click(clear_chat, outputs=[msg, chatbot])


# -------------------- LAUNCH --------------------
page.launch(
    theme=gr.themes.Soft(),
    share=True
)