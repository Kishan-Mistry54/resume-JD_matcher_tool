# Resume-JD_matcher_tool
An AI-powered tool that compares a candidate's resume against a job description (JD), extracts relevant skills dynamically, and produces a weighted match score with a narrative explanation.

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
resume-jd-matcher/├── .gitignore          # Ignores API keys and cache├── .env.example        # Template for required API keys├── index.html          # Frontend UI├── server.py           # Flask backend (API endpoints, LLM logic)├── requirements.txt    # Python dependencies└── README.md           # Project documentation
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


---

### Final Checklist Before You Submit:
1. [ ] Deleted `app.py`, `skill_dictionary.py`, `explainer.py`, `scorer.py`, `skill_extractor.py`, `test_key.py`, and `__pycache__`.
2. [ ] Created `.gitignore` with `.env` and `__pycache__` inside it.
3. [ ] Created `.env.example` with the dummy key inside it.
4. [ ] Created `README.md`.
5. [ ] Made sure your **real** `.env` file is safely on your computer and NOT in the GitHub repo.

Once you push this to GitHub, it looks incredibly professional. It shows you understand clean code, frontend/backend separation, security (hiding API keys), and documentation.
make a space where i can put ss oof my project 

Thought Process
Here is exactly how to add a screenshots section to make your GitHub repo look complete and professional.

Step 1: Create a folder for images
Inside your resume-jd-matcher folder, create a new folder and name it exactly:
screenshots

Step 2: Take your screenshots
Run your project (python server.py), open it in your browser, and take 2 screenshots:

Input View: The page showing the "Choose PDF" buttons and text areas before clicking analyze. Name this image input.png
Results View: The page showing the score, green/red skill tags, and the explanation. Name this image results.png
Put both images inside that screenshots folder.

Step 3: Update your README.md
Open your README.md file and add the screenshot section right below the "Problem Solved" section.

Here is the updated README.md (copy and replace your current one):

Resume–JD Matching Tool
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
