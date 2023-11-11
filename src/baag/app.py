import streamlit as st
import io
import pdfplumber
import openai
from keys import OPEN_API_KEY

# Set your API key
openai.api_key = OPEN_API_KEY

# Define the model you want to use
MODEL_NAME = "text-davinci-003"
MAX_TOKENS = 100

# Page Configuration
st.set_page_config(page_title="PDF Summarizer", page_icon=":arrow_up:", layout="wide")

# Header
st.title("PDF Summarizer")


def summarize_pdf_text(pdf_text: str) -> str:
    try:
        # Tokenize and split the text into manageable chunks if needed
        # For simplicity, this example does not include chunking logic
        # You might need to add logic to handle long texts

        # Call the OpenAI API to summarize
        response = openai.Completion.create(
            model=MODEL_NAME,
            prompt=f"Summarize this document with {MAX_TOKENS} max tokens: {pdf_text}",
            max_tokens=MAX_TOKENS,  # Adjust based on your needs
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return ""


def read_pdf(file):
    try:
        with pdfplumber.open(file) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        return "\n".join(pages)
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""


uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Reading PDF..."):
        with io.BytesIO(uploaded_file.getbuffer()) as file_stream:
            pdf_text = read_pdf(file_stream)

    if pdf_text:
        with st.spinner("Summarizing..."):
            summary = summarize_pdf_text(pdf_text)
            st.markdown(summary)
