import streamlit as st
from chatbot import run_chatbot

st.set_page_config(page_title="LangChain Chatbot", layout="centered", initial_sidebar_state="collapsed")
st.title("🧠 LangChain Chatbot")

# Session state for conversation
if "history" not in st.session_state:
    st.session_state.history = []

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Ask about S3, upload files, etc.")
    submit = st.form_submit_button("Send")

if submit and user_input:
    with st.spinner("Thinking..."):
        response = run_chatbot(user_input)
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", response))

# Display chat history
for speaker, msg in reversed(st.session_state.history):
    st.markdown(f"**{speaker}:** {msg}")

