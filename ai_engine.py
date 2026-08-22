import os

from dotenv import load_dotenv
from google import genai


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# ============================================================
# CHECK API KEY
# ============================================================

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file. "
        "Please add your Gemini API key."
    )


# ============================================================
# CREATE GEMINI CLIENT
# ============================================================

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ============================================================
# ANALYZE CANDIDATE
# ============================================================

def analyze_candidate(candidate, job_description):

    prompt = f"""
You are an AI recruitment assistant.

Your task is to analyze a candidate against a job description.

IMPORTANT RULES:

- Use only the information provided.
- Do not invent candidate information.
- Do not assume missing experience or skills.
- Do not make decisions based on gender, age, religion,
  race, marital status, disability, or other protected
  characteristics.
- The recommendation should support human recruiters,
  not replace human decision-making.


============================================================
JOB DESCRIPTION
============================================================

{job_description}


============================================================
CANDIDATE INFORMATION
============================================================

Candidate ID:
{candidate['candidate_id']}

Candidate Name:
{candidate['name']}

Education:
{candidate['education']}

Experience:
{candidate['experience_years']} years

Skills:
{candidate['skills']}

Projects:
{candidate['projects']}

Certifications:
{candidate['certifications']}

Candidate Summary:
{candidate['summary']}


============================================================
ANALYSIS REQUIRED
============================================================

Please provide the following sections:

1. Candidate Summary

2. Match Score
Give a score from 0 to 100.

3. Matching Skills
List the skills that match the job requirements.

4. Missing Skills
List important job requirements that are not found
in the candidate information.

5. Candidate Strengths
List the main strengths relevant to this position.

6. Candidate Weaknesses
List relevant areas where the candidate may need improvement.

7. Recommendation

Choose exactly one:

SHORTLIST
CONSIDER
REJECT

8. Recommendation Explanation
Explain briefly why the recommendation was made.

9. Interview Questions
Generate 3 relevant interview questions based on
the candidate's skills and the job requirements.


Remember:
Do not invent information.
Use only the candidate information provided.
"""


    # ========================================================
    # SEND REQUEST TO GEMINI
    # ========================================================

    response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)


    # ========================================================
    # RETURN AI RESPONSE
    # ========================================================

    return response.text