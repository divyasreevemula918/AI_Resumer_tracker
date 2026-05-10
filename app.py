from utils.parser import extract_text_from_pdf
from agents.analyser import analyze_resume
from agents.skill_extractor import extract_skills
from utils.similarity import calculate_similarity
from agents.interview_generator import generate_questions
import streamlit as st

st.set_page_config(page_title="AI Resume Analyzer")

st.title("💼 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Extracted Resume Text")
    st.write(resume_text[:1500])

    skills = extract_skills(resume_text)

    st.subheader("🧠 Detected Skills")
    st.write(skills)

    if job_description:

        similarity = calculate_similarity(
            resume_text,
            job_description
        )

        st.subheader("📊 Resume Match Score")
        st.write(f"{similarity}%")

        analysis = analyze_resume(
            resume_text,
            job_description
        )

        st.subheader("🤖 AI Analysis")
        st.write(analysis)

        questions = generate_questions(resume_text)

        st.subheader("🎯 Interview Questions")
        st.write(questions)