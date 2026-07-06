from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import PyPDF2

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory(os.path.dirname(__file__), 'index.html')

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)
MODEL = "llama-3.1-8b-instant"

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + " "
    return text

def call_llm(prompt, system_prompt=None, json_mode=False):
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    kwargs = {"model": MODEL, "messages": messages, "temperature": 0.2}
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}
        
    response = client.chat.completions.create(**kwargs)
    return response.choices[0].message.content

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        resume_file = request.files.get('resume')
        jd_file = request.files.get('jd')
        resume_text = request.form.get('resume_text', '')
        jd_text = request.form.get('jd_text', '')

        # Extract text from PDFs if uploaded, otherwise use pasted text
        if resume_file and resume_file.filename.endswith('.pdf'):
            resume_text = extract_text_from_pdf(resume_file)
        if jd_file and jd_file.filename.endswith('.pdf'):
            jd_text = extract_text_from_pdf(jd_file)

        if not resume_text.strip() or not jd_text.strip():
            return jsonify({"error": "Please provide both resume and JD text or PDFs."}), 400

        # 1. Extract Skills using ONLY LLM
        sys_extract = """You are an expert technical recruiter. Extract ALL technical skills, programming languages, frameworks, libraries, tools, platforms, and methodologies mentioned in the text. 
        Return a JSON object with a single key "skills" containing a list of lowercase strings. 
        Example: {"skills": ["python", "machine learning", "aws", "docker", "rest apis"]}"""

        try:
            res_resp = call_llm(f"Extract skills from this resume:\n{resume_text[:3000]}", sys_extract, True)
            resume_skills = list(set(json.loads(res_resp).get("skills", [])))
        except:
            resume_skills = []

        try:
            jd_resp = call_llm(f"Extract skills from this job description:\n{jd_text[:3000]}", sys_extract, True)
            jd_skills = list(set(json.loads(jd_resp).get("skills", [])))
        except:
            jd_skills = []

        # 2. Compute Score & Match using LLM Semantic Understanding
        sys_score = """You are a skill matching assistant. Compare the resume skills to the job description skills.
        Determine which JD skills are covered by the resume (exact or semantic match, e.g., "pytorch" covers "deep learning framework").
        Return JSON exactly like this: 
        {"matched": ["skill1", "skill2"], "missing": ["skill3", "skill4"]}"""
        
        score_prompt = f"Resume skills: {json.dumps(resume_skills)}\n\nJob Description skills: {json.dumps(jd_skills)}"
        try:
            score_resp = call_llm(score_prompt, sys_score, True)
            score_data = json.loads(score_resp)
            all_matched = list(set(score_data.get("matched", [])))
            all_missing = list(set(score_data.get("missing", [])))
        except:
            all_matched = [s for s in jd_skills if s in resume_skills]
            all_missing = [s for s in jd_skills if s not in resume_skills]
        
        final_score = round((len(all_matched) / max(len(jd_skills), 1)) * 100)

        # 3. Generate Explanation
        sys_exp = "You are a career advisor. Write a brief 4-6 sentence explanation of the match. Mention specific matched and missing skills, and give actionable advice."
        exp_prompt = f"Score: {final_score}/100. Matched: {json.dumps(all_matched)}. Missing: {json.dumps(all_missing)}. Explain this match."
        
        try:
            explanation = call_llm(exp_prompt, sys_exp)
        except:
            explanation = f"Match is {final_score}%. Key missing skills: {', '.join(all_missing[:5])}."

        return jsonify({
            "score": final_score,
            "matched": all_matched,
            "missing": all_missing,
            "explanation": explanation
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)