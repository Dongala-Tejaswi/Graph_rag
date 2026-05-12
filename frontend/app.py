import streamlit as st
import requests

st.title("Graph RAG Assistant")

query = st.text_input(
    "Ask your question"
)

if st.button("Submit"):

    response = requests.post(
        "http://localhost:8000/ask",
        json={"query": query}
    )

    data = response.json()

    st.subheader("Answer")

    st.write(data["answer"])