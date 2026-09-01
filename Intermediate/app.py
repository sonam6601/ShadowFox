import streamlit as st
from pypdf import PdfReader
from dotenv import load_dotenv
from google import genai
import os

# Load API key from .env
load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

# Check API key
if not api_key:
    st.error("❌ Gemini API key not found. Please check your .env file.")
    st.stop()

# Page settings
st.set_page_config(
    page_title="Document Q&A Assistant",
    page_icon="📄"
)

# Gemini client
client = genai.Client(api_key=api_key)

# App title
st.title("📄 Document Q&A Assistant")
st.write("Upload a PDF and ask questions from its content.")

# PDF upload
uploaded_file = st.file_uploader(
    "📤 Upload your PDF",
    type=["pdf"]
)

if uploaded_file:

    # Read PDF
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    # Success message
    st.success("✅ PDF uploaded successfully!")

    st.write("📄 Number of pages:", len(reader.pages))

    # Question input
    question = st.text_input(
        "❓ Ask a question about your document:"
    )

    # Generate answer
    if question:

        with st.spinner("🤖 Generating answer..."):

            prompt = f"""
You are a helpful document assistant.

Answer the user's question using ONLY the information
available in the uploaded document.

If the answer is not available in the document,
say exactly:

"The answer is not available in the uploaded document."

DOCUMENT:
{text}

QUESTION:
{question}
"""

            try:
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )

                st.subheader("🤖 Answer")
                st.write(response.text)

            except Exception as e:
                st.error("❌ Error while generating answer.")
                st.write(str(e))