# 🧠 AI Resume Screener (Ollama-Powered)

This project is an AI-powered resume analyzer that compares a resume with a job description and provides:
- A match score (out of 100)
- 3 actionable suggestions to improve the resume

It runs **completely offline** using **Mistral LLM** on **Ollama**, and has a clean frontend built using **Streamlit**.

---

## 🚀 Features

✅ Upload resume (PDF)  
✅ Paste job description  
✅ Instant AI response  
✅ No API key needed — works 100% locally  
✅ Clear, professional output with suggestions  

---

## 🧰 Tech Stack

| Component | Tool |
|----------|------|
| 💻 UI | Streamlit |
| 🧠 LLM | Mistral via Ollama |
| 📄 Resume Parsing | PyMuPDF |
| 🔗 Backend Calls | Python `requests` |

---

## ⚙️ Setup & Run

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/resume-screener-ai.git
cd resume-screener-ai