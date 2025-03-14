import streamlit as st
from gemini_model import conversation

# Streamlit UI setup
st.set_page_config(page_title="AI Data Science Tutor", layout="wide")

st.title("🤖 AI Conversational Data Science Tutor")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask your data science question...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    response = conversation.run(user_input)

    # Display AI message
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
