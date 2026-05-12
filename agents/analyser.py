from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)

prompt = PromptTemplate(
    input_variables=["resume_text", "job_description"],
    template="""
You are an expert ATS resume analyzer.

Analyze the following resume.

Resume:
{resume_text}

Job Description:
{job_description}

Provide:
1. ATS Score out of 100
2. Missing Skills
3. Resume Summary
4. Suggested Improvements
5. Strengths
6. Weaknesses
"""
)

chain = prompt | llm


def analyze_resume(resume_text, job_description):

    response = chain.invoke({
        "resume_text": resume_text,
        "job_description": job_description
    })

    return response.content