# Resume-JD Matcher Tool

An AI-powered tool that compares a candidate's resume against a job description (JD), extracts relevant skills dynamically, and produces a weighted match score with a narrative explanation.

📸 Screenshots
1. Uploading / Pasting Data
Input View


2. Match Results & Explanations
Results View


Problem Solved
Manually comparing resumes to job descriptions is time-consuming and prone to human bias. This tool automates the process by using an LLM to understand the semantic meaning of skills (e.g., knowing that "PyTorch" satisfies a requirement for "deep learning frameworks"), rather than just doing dumb keyword matching.

Key Features
Dual Input: Accepts raw text or direct PDF uploads for both Resumes and JDs.
Dynamic Skill Extraction: Uses an LLM to extract skills, ensuring it catches new or non-standard technologies without needing a hardcoded dictionary.
Semantic Matching: Intelligently matches skills rather than relying solely on exact string matches.
Weighted Scoring: Outputs a clear 0–100 match score.
Visual Breakdown: Clean UI showing green (matched) and red (missing) skill tags.
Actionable Feedback: Generates a short, specific explanation of the match and what the candidate is missing.
Tech Stack
Backend: Python, Flask
Frontend: HTML, CSS, Vanilla JavaScript
AI/LLM: Groq API (Llama 3.1 8B)
PDF Parsing: PyPDF2
Environment: python-dotenv
Project Structure
resume-jd-matcher/├── .gitignore          # Ignores API keys and cache├── .env.example        # Template for required API keys├── index.html          # Frontend UI├── server.py           # Flask backend (API endpoints, LLM logic)├── requirements.txt    # Python dependencies├── README.md           # Project documentation└── screenshots/        # Project images    ├── input.png    └── results.png
Setup & Running Locally
Clone the repository:
bash

git clone <your-repo-link>
cd resume-jd-matcher
Create a virtual environment (Recommended):
bash

python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
Install dependencies:
bash

pip install -r requirements.txt
Set up environment variables:
Rename .env.example to .env
Add your Groq API key (get a free one at console.groq.com):
env

GROQ_API_KEY=gsk_your_actual_key_here
Run the application:
bash

python server.py
The server will start on http://127.0.0.1:5000. Open that URL in your browser to use the tool.
Deployment Note
This application is designed to run locally. It can be easily deployed to platforms like Render or Railway by connecting the GitHub repo and adding the GROQ_API_KEY to the platform's environment variables.

text


### Your final folder structure will look like this:
```text
resume-jd-matcher/
├── .gitignore
├── .env.example
├── index.html
├── server.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── input.png       <-- You add this
    └── results.png     <-- You add this
When you push this to GitHub, the README will automatically display the images nicely right at the top. It makes the project look highly polished for the E2S assessment.



