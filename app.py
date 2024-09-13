import streamlit as st
from backend import *

st.title("Vanilla RAG Q/A Bot")

uploaded_file = st.file_uploader("Upload a PDF or Word document", type=['pdf', 'docx'])
if uploaded_file is not None:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File uploaded successfully!")
    user_query = st.text_input("Enter your question:")  
    if st.button("Get Answer"):
        if user_query:
            answer = RAGBot(uploaded_file.name, user_query)
            st.write(f"Answer: {answer}")
        else:
            st.write("Please enter a question.")