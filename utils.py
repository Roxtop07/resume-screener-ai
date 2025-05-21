import requests

def generate_feedback(resume, jd):
    prompt = f"""
You are a professional AI Resume Screener.

Compare the following resume with the job description and strictly respond in this format:

Score: <Give a score out of 100>

Suggestions:
1. <First suggestion>
2. <Second suggestion>
3. <Third suggestion>

Do not add any extra information or explanation.

---

Resume:
{resume}

---

Job Description:
{jd}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )
    
    data = response.json()
    output = data["response"]

    # Simple parsing
    lines = output.strip().split("\n")
    score = next((line.split(":")[-1].strip() for line in lines if "score" in line.lower()), "N/A")
    suggestions = [line.strip("•-123. ") for line in lines if line.strip().startswith(("1", "2", "3"))]
    
    return {
        "score": score,
        "suggestions": suggestions[:3]  # Optional trimming
    }