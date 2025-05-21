import streamlit as st
from resume_parser import extract_text_from_pdf
from utils import generate_feedback

st.set_page_config(page_title="AI Resume Screener", page_icon="🧠")

st.title("🧠 AI Resume Screener (Ollama Version)")

resume_file = st.file_uploader("📄 Upload your Resume (PDF only)", type=["pdf"])
jd_text = st.text_area("🧾 Paste the Job Description")

if st.button("🚀 Analyze") and resume_file and jd_text:
    with st.spinner("Processing..."):
        resume_text = extract_text_from_pdf(resume_file)
        result = generate_feedback(resume_text, jd_text)

        st.subheader("✅ Match Score:")
        st.write(f"🔢 {result['score']} / 100")

        st.subheader("📌 Suggestions to Improve Resume:")
        for i, suggestion in enumerate(result['suggestions'], start=1):
            st.markdown(f"{i}. {suggestion}") 