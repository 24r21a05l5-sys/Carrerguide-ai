import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    temperature=0.3,
    model_name="llama-3.1-8b-instant",
    groq_api_key=st.secrets.get("GROOQ_API_KEY")
)

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def analyze_resume_vs_jd(resume_text, job_description):
    vectorstore = FAISS.from_texts([resume_text], embeddings)
    retriever = vectorstore.as_retriever()
    relevant_docs = retriever.invoke(job_description)
    context = "\n".join([doc.page_content for doc in relevant_docs])

    prompt = PromptTemplate.from_template(
        """You are an expert HR Manager and Career Coach.

Job Description:
{jd}

Candidate Resume Context:
{context}

Analyze the resume strictly against the Job Description and provide:
1. Match Score: A percentage (0-100%).
2. Missing Skills & Keywords: Key technical or soft skills present in JD but missing in Resume.
3. Bullet Point Improvements: Identify 2 weak bullet points from the resume and rewrite them using the STAR Method (Situation, Task, Action, Result) with quantitative impact metrics."""
    )

    chain = prompt | llm
    response = chain.invoke({"jd": job_description, "context": context})
    return response.content

def generate_interview_questions(job_description):
    prompt = PromptTemplate.from_template(
        """Based on the following Job Description, generate 5 technical and situational interview questions with ideal brief answer tips.

Job Description:
{jd}"""
    )
    chain = prompt | llm
    response = chain.invoke({"jd": job_description})
    return response.content
def generate_low_match_guidance(match_score, job_description):
    prompt = PromptTemplate.from_template(
        """You are a supportive, chill, and encouraging tech-savvy college friend. 
        The student's resume match score is low ({match_score}%).
        
        Give them direct, honest, yet super encouraging advice like a best friend talking to them. Avoid formal corporate jargon.
        
        Structure your advice simply:
        1. **Missing Skills/Projects:** Chill check on what tools or projects they should build.
        2. **Quick Learnings:** Simple certifications or topics to cover quickly.
        3. **Resume Fix:** Simple tip on how to reframe their existing experience for this JD: {jd}
        
        End on a super positive note like "You've got this! Let's build this together!"
        """
    )
    chain = prompt | llm
    response = chain.invoke({"match_score": match_score, "jd": job_description})
    return response.content

