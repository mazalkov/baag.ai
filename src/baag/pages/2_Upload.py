import streamlit as st
import pandas as pd
import io
import pdfplumber

import openai
from keys import OPEN_API_KEY

# Set your API key
openai.api_key = OPEN_API_KEY

# Define the model you want to use (e.g., "text-davinci-003")
model_name = "text-davinci-003"

# Page Configuration
st.set_page_config(page_title="Upload", page_icon=":arrow_up:", layout="wide")

# Header
st.title("Upload files for analysis")

# uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
# for uploaded_file in uploaded_files:
#     bytes_data = uploaded_file.read()
#     st.write("filename:", uploaded_file.name)


def summarise(prompt: str) -> str:
    # Get the response from the model
    response = openai.Completion.create(model=model_name, prompt=prompt, max_tokens=60)

    return response.choices[0].text.strip()


def read_pdf(file):
    with pdfplumber.open(file) as pdf:
        pages = [page.extract_text() for page in pdf.pages]
    return "\n".join(pages)


uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # To read file as stream:
    with io.BytesIO(uploaded_file.getbuffer()) as file_stream:
        text = read_pdf(file_stream)

        summary = summarise(text)

        st.markdown(summary)
