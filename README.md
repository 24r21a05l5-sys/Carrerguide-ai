# 📄 AI-Powered Resume Analyzer & Career Coach

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)
![Llama 3](https://img.shields.io/badge/Llama_3-Groq_API-orange?style=for-the-badge)

An end-to-end intelligent career assistance application built with **Streamlit**, **LangChain**, and **Llama-3 via Groq API**. It uses **Retrieval-Augmented Generation (RAG)** architecture to analyze resumes against job descriptions and provides instant match scoring, missing keyword analysis, and actionable optimization strategies.

---

[🚀 Live Demo](https://ai-resume-analyzer-rag.streamlit.app) · [📹 Video Demo](https://linkedin.com) · [🐛 Report Issue](https://github.com/your-username/ai-resume-analyzer-rag/issues)

---

## Key Features

* **Automated ATS & Alignment Scoring:** Evaluates resume content against job requirements to generate an accurate match percentage.
* **Gap & Keyword Analysis:** Identifies critical missing technical skills, keywords, and domain-specific terminology.
* **Actionable Resume Optimization:** Provides tailored recommendations using the STAR (Situation, Task, Action, Result) framework.
* **Ultra-Low Latency:** Leverages Groq's LPU Inference Engine for real-time AI responses within seconds.
* **Custom AI Model Integration:** Features a specialized, custom-generated/fine-tuned AI model optimized specifically for deep document parsing and resume-to-JD contextual evaluation.
*
---

## Tech Stack & Architecture

* **Frontend:** Streamlit
* **LLM Orchestration:** LangChain Framework
* **AI Model Engine:** Custom-Trained / Generated Model + Groq API (Llama-3)
* **Architecture:** RAG (Retrieval-Augmented Generation)
* **Programming Language:** Python 3.10+

---

## Getting Started

### Prerequisites
Ensure you have **Python 3.10** or higher installed on your system along with an active **Groq API Key**.

### 1. Repository Setup
Clone the repository directly from [GitHub Repository](https://github.com/hashmizareen86-spec/ai-resume-analyzer-rag):

```bash
git clone [https://github.com/hashmizareen86-spec/ai-resume-analyzer-rag.git](https://github.com/hashmizareen86-spec/ai-resume-analyzer-rag.git)
cd ai-resume-analyzer-rag

2. Environment Configuration
Windows:
python -m venv venv
venv\Scripts\activate

3. macOS/Linux:
python3 -m venv venv
source venv/bin/activate

##Usage Workflow##
Upload Resume: Drag and drop any software engineering/technical resume in .pdf format.

Paste Job Description: Enter the target job posting text into the JD input area.

Analyze: Click "Analyze & Score" to generate an instant breakdown of:
Overall ATS Compatibility Percentage
Missing Technical & Soft Keywords
Key Strengths & Tailored Recommendations
Interactive Chat: Switch to the Chatbot Tab to ask custom questions about the resume's contents.

##Roadmap & Future Improvements##
-[ ] Multi-resume bulk screening for recruiters.
-[ ] Integration with open-source local LLMs via Ollama (llama3 / mistral).
-[ ] Automated LaTeX/Markdown output generator for restructured resumes.

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a Pull Request.
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AwesomeFeature`)
3. Commit your Changes (`git commit -m 'Add some AwesomeFeature'`)
4. Push to the Branch (`git push origin feature/AwesomeFeature`)
5. Open a Pull Request

