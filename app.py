import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

from rag_pipeline import retrieve_context
from gemini_client import generate_answer

@st.cache_resource
def load_rag():
    return retrieve_context, generate_answer

retrieve_context, generate_answer = load_rag()

st.set_page_config(
    page_title="ASU Student Support Chatbot",
    page_icon="🎓",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("🎓 ASU Chatbot")
    st.markdown("---")
    st.write("AI-powered Student Support Assistant")
    st.markdown("### Features")
    st.write("✅ Semantic Search")
    st.write("✅ FAISS Retrieval")
    st.write("✅ Gemini AI")
    st.write("✅ RAG Pipeline")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🎓 Arizona State University Student Support Chatbot")

# Show old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask anything about Arizona State University...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Searching University Knowledge Base..."):

        context = retrieve_context(prompt)

        answer = generate_answer(
            context,
            prompt
        )

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)