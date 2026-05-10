from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-8b-8192"
)

prompt = PromptTemplate(
    input_variables=["resume_text"],
    template="""
Generate 10 interview questions based on this resume.

Resume:
{resume_text}
"""
)

chain = prompt | llm


def generate_questions(resume_text):

    response = chain.invoke({
        "resume_text": resume_text
    })

    return response.content