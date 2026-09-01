Production RAG Assistant

Introduction

Production RAG Assistant is a document question-answering application. It allows users to upload PDF documents and ask questions based on the information available in those documents.

The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate clear answers using an AI model.

Features

- Upload PDF documents
- Extract text from PDF files
- Split and store document information
- Store documents in ChromaDB
- Retrieve relevant information for user questions
- Generate answers using Gemini
- Display source documents and page numbers
- Simple web-based frontend
- FastAPI backend

Technologies Used

- Python
- FastAPI
- ChromaDB
- Google Gemini
- Pydantic
- PyPDF
- HTML
- CSS
- JavaScript

Project Workflow

PDF Upload
     ↓
Text Extraction
     ↓
Document Processing
     ↓
ChromaDB
     ↓
User Question
     ↓
Relevant Information Retrieval
     ↓
Gemini
     ↓
Answer + Sources

Project Structure

Production-RAG-Assistant
│
├── app
│   ├── api
│   ├── core
│   ├── ingestion
│   ├── llm
│   ├── models
│   ├── retrieval
│   ├── workflow
│   └── main.py
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── uploads
├── chroma_db
├── requirements.txt
├── .env
└── README.md

How to Run

1. Install dependencies

pip install -r requirements.txt

2. Configure environment variables

Create a ".env" file and add the required Google API key.

GOOGLE_API_KEY=your_api_key_here

3. Start the backend

python -m uvicorn app.main:app

The API will run at:

http://127.0.0.1:8000

4. Open the frontend

Open the frontend using Live Server and use the web interface to upload a PDF and ask questions.

Example

User uploads a PDF document and asks:

What is the internship duration?

The system retrieves the relevant information from the document and generates an answer using Gemini.

Conclusion

This project demonstrates how Retrieval-Augmented Generation can be used to build a document-based AI assistant. It combines document processing, vector search, an AI language model, and a web interface into one application.