import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def app_response(input, prompt):
    model= genai.GenerativeModel("gemini-pro")
    response= model.generate_content(input)
    return response.text

def preprocess_pdf(resume):
    reader = pdf.PdfReader(resume)
    text=""
    for page in range(len(reader.pages)):
        page= reader.pages[page]
        text += str(page.extract_text())
        return text

prompt= """
        Act like a professional and experienced ATS (Application Tracking System) with a deep understanding
        of the tech field such as data science, artificial intelligence engineering, software engineering, 
        data analysis, big data engineering and ui/ux designer. 
        You are to evaluate every resume given based on the given job description(jd). Provide the best assistance 
        to improve the resume, give the percentage at which the resume matches the jd, state the missing 
        keywords in the resume and explain concisely how to improve my skills. Do all these tasks 
        with one hundred percent accuracy. Strictly give the response in the format given below

        Job description match: ""
        Missing Keywords: ""
        Profile Summary: ""
        How to improve required skills: ""

        """
st.set_page_config(page_title="ATS Application")   
st.title("ATS Apllication")
st.text("Improve your resume")

jd= st.text_area("Enter the Job Description")
resume_upload= st.file_uploader("Upload a resume", type= "pdf", help="Please upload a resume")

submit= st.button("submit")
if submit:
    if resume_upload is not None:
        text= preprocess_pdf(resume_upload)
        response= app_response(prompt, text)
        st.subheader("Response:")
        st.write(response)  






















