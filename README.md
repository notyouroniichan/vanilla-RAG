# Vanilla RAG Q/A Bot

## Overview

This project implements a Retrieval-Augmented Generation (RAG) bot that can process documents and answer user queries based on the content of these documents. The bot extracts text from PDF or DOCX files, splits it into chunks, and creates a vector store for efficient retrieval. The RAG model is used to generate detailed answers based on the retrieved information.

## Features

- **Document Extraction**: Extracts text from PDF and DOCX files.
- **Text Chunking**: Splits text into manageable chunks for processing.
- **Vector Store Creation**: Uses FAISS and HuggingFace embeddings for efficient document retrieval.
- **RAG Model**: Leverages a RAG model for answering queries with detailed responses.

## Installation

### Prerequisites

- Python 3.8 or later
- `pip` (Python package installer)

### Required Libraries

1. Install the necessary Python libraries using `pip`:

    ```bash
    pip install PyPDF2 python-docx langchain transformers faiss-cpu python-dotenv
    ```

2. Create a `.env` file in the root directory of your project and add your Hugging Face API token:

    ```
    HUGGING_FACE_API=your_hugging_face_api_token_here
    ```
## Functions

- **```extractPDF(file_path)```:** Extracts text from a PDF file.
- **```extractWord(file_path)```:** Extracts text from a DOCX file.
- **```processDocument(file_path)```:** Determines the file type and extracts text accordingly.
- **```createChunks(text)```:** Splits the extracted text into chunks.
- **```createVector(documents)```:** Creates a vector store from the text chunks.
- **```setupRAG(vector_store)```:** Sets up the RAG model using HuggingFaceHub.
- **```RAGBot(file_path, user_query)```:** Main function that processes the document and answers the user's query.

## Running the Bot

After installing the necessary libraries and adding your Hugging Face API token. Navigate to you root folder and run the command :
```
streamlit run app.py
```