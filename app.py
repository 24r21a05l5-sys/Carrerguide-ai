import streamlit as st
from gtts import gTTS
import requests
from streamlit_lottie import st_lottie
from rag_engine import generate_low_match_guidance
from utils import extract_text_from_pdf
from rag_engine import analyze_resume_vs_jd, generate_interview_questions
import streamlit.components.v1 as components
st.set_page_config(page_title="AI Career Coach", layout="wide")

st.title("AI Career Coach & Resume Assistant")
st.caption("Optimize your resume against job descriptions using RAG & Llama-3")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])

with col2:
    st.subheader("Job Description")
    job_desc = st.text_area("Paste the Target Job Description here...", height=180)

if st.button("Analyze Alignment", type="primary"):
    if uploaded_file and job_desc:
        with st.spinner("Extracting text and running RAG analysis..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            analysis_result = analyze_resume_vs_jd(resume_text, job_desc)
            st.divider()
            st.subheader("Match Analysis & Recommendations")
            st.markdown(analysis_result)
            # Low match guidance logic
        if "Match Score: 7" not in analysis_result and "Match Score: 8" not in analysis_result and "Match Score: 9" not in analysis_result:
            st.warning("⚠️ Low Match Detected! Here is your AI Coach's Guidance:")
            guidance = generate_low_match_guidance("Low", job_desc)
            
            g1, g2 = st.columns([1.2, 0.8])
            with g1:
                st.markdown("### 🎯 Recommended Action Plan")
                st.write(guidance)
                
                tts = gTTS(text="Your resume match score is low. Check out the recommended roadmap to bridge the gap!", lang='en')
                tts.save("coach_voice.mp3")
                st.audio("coach_voice.mp3", format="audio/mp3")

            with g2:
                lottie_url = "https://assets5.lottiefiles.com/packages/lf20_m6487122.json"
                try:
                    lottie_json = requests.get(lottie_url).json()
                    if lottie_json:
                        st_lottie(lottie_json, height=250, key="coach_avatar")
                except:
                    st.info("🤖 AI Coach Active")
    else:
        st.warning("Kripya Resume PDF aur Job Description dono provide karein.")

st.divider()
if st.button("Generate Mock Interview Questions"):
    if job_desc:
        with st.spinner("Questions generate ho rahe hain..."):
            questions = generate_interview_questions(job_desc)
            st.subheader("Tailored Interview Prep")
            st.markdown(questions)
    else:
        st.warning("Interview questions ke liye Pehle Job Description daalein.")
        # --- D-ID Live AI Mentor Section ---
st.divider()
st.subheader("💬 Interactive AI Mentor")

# Exact D-ID Agent Direct Embed URL
# Working D-ID Public Share Link
agent_url = "https://studio.d-id.com/agents/share?id=v2_agt_0NS_8x8s&key=ck_ijlwrlEp23dEXUelSkMSa"

components.iframe(agent_url, height=600, scrolling=True)

