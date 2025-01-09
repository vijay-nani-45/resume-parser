import streamlit as st
from model.parser import ResumeParser
from utils.text_processor import preprocess_text, extract_sections
import PyPDF2
import io

def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def main():
    st.title("Resume Parser")
    st.write("Upload a resume to extract key information")

    uploaded_file = st.file_uploader("Choose a resume file", type=["txt", "pdf"])

    if uploaded_file is not None:
        # Read and preprocess the resume text
        if uploaded_file.type == "application/pdf":
            text = read_pdf(io.BytesIO(uploaded_file.getvalue()))
        else:
            text = uploaded_file.getvalue().decode("utf-8")

        preprocessed_text = preprocess_text(text)
        sections = extract_sections(preprocessed_text)

        # Parse the resume
        parser = ResumeParser()
        result = parser.parse_resume(text)

        # Display results
        st.subheader("Extracted Information")
        st.write(f"Name: {result['name']}")
        st.write(f"Email: {result['email']}")
        st.write(f"Phone: {result['phone']}")
        st.write("Skills:", ", ".join(result['skills']))
        st.write("Education:")
        for edu in result['education']:
            st.write(f"- {edu}")

        # Display extracted sections
        st.subheader("Resume Sections")
        for section, content in sections.items():
            st.write(f"{section.capitalize()}:")
            for item in content:
                st.write(f"- {item}")

if __name__ == "__main__":
    main()

