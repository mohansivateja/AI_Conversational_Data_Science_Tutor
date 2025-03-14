import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Set up API key
import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyDtYYx93whP34ue58kvc583I-_xTvCEsrk"

# Initialize memory
memory = ConversationBufferMemory(memory_key="chat_history")

# Define the system prompt
template = """
You are an AI Data Science Tutor. You will answer only data science-related queries.
If the user asks something outside of data science, politely decline.

Conversation history:
{chat_history}

User: {question}
AI:
"""

prompt = PromptTemplate(input_variables=["chat_history", "question"], template=template)

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Create conversation chain with memory
conversation = LLMChain(llm=llm, prompt=prompt, memory=memory)
