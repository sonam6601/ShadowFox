import streamlit as st
from google import genai

# Page settings
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚"
)

st.title("📚 AI Study Assistant")
st.write("Your personal AI-powered study helper")

# Gemini client
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
    st.error("Gemini API connection failed. Please check your API key.")
    st.stop()

# User input
notes = st.text_area(
    "Enter your notes or question:",
    height=200,
    placeholder="Paste your notes or type your question here..."
)

# Feature selection
feature = st.selectbox(
    "Choose a feature:",
    [
        "Summarize Notes",
        "Explain Topic",
        "Generate Quiz",
        "Improve Answer"
    ]
)

# Generate response
if st.button("Generate"):

    if not notes.strip():
        st.warning("Please enter some notes or a question first.")
        st.stop()

    # Create structured prompt
    if feature == "Summarize Notes":
        prompt = f"""
You are an AI study assistant.

Task: Summarize the student's notes.

Instructions:
- Keep the summary simple and clear.
- Include the important points.
- Use short paragraphs or bullet points.

Student Notes:
{notes}
"""

    elif feature == "Explain Topic":
        prompt = f"""
You are an AI study assistant.

Task: Explain the following topic in simple language.

Instructions:
- Explain it clearly.
- Use an example if helpful.
- Make it suitable for a college student.

Topic:
{notes}
"""

    elif feature == "Generate Quiz":
        prompt = f"""
You are an AI study assistant.

Task: Create 5 useful quiz questions from the student's notes.

Instructions:
- Include the correct answer after each question.
- Keep the questions relevant to the notes.
- Use simple language.

Student Notes:
{notes}
"""

    else:
        prompt = f"""
You are an AI study assistant.

Task: Improve the following student answer.

Instructions:
- Make it clearer.
- Correct grammar.
- Make it more informative.
- Do not change the original meaning.

Student Answer:
{notes}
"""

    # Generate AI response
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        st.subheader("🤖 AI Response")

        if response.text:
            st.write(response.text)
        else:
            st.warning("The AI returned an empty response. Please try again.")

    except Exception as e:
        st.error("Sorry, the AI service could not generate a response.")
        st.write("Please check your internet connection and try again.")