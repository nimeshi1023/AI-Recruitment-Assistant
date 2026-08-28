# 🤖 AI Recruitment Assistant

## Generative AI Application

An AI-powered recruitment assistant that uses Generative AI to analyze candidate profiles against job descriptions and provide structured recruitment insights.

This project was developed as an individual Generative AI application for a recruitment/HR business use case.

---

## 📌 Project Overview

Recruiters often need to review many candidate profiles and compare them with job requirements. Manual screening can be time-consuming.

The **AI Recruitment Assistant** uses a Large Language Model (LLM) through the Google Gemini API to analyze candidate information and generate:

- Candidate summary
- Match score
- Matching skills
- Missing skills
- Candidate strengths
- Candidate weaknesses
- Recruitment recommendation
- Recommendation explanation
- Interview questions

The system is designed as a **decision-support tool** for recruiters. It does not replace human decision-making.

---

## 🎯 Business Use Case

### Recruitment / Human Resources

The application supports the initial screening stage of recruitment.

A recruiter can provide:

1. A job description
2. Candidate information

The AI then compares the candidate profile with the job requirements and generates a structured assessment.

This can help recruiters:

- Reduce repetitive screening work
- Quickly identify relevant skills
- Identify missing qualifications
- Prepare interview questions
- Prioritize candidates for further human review

---

## 🎯 Objectives

The main objectives of this project are:

- Build a simple Generative AI application.
- Apply Generative AI to a real-world recruitment use case.
- Use an LLM API to analyze candidate information.
- Compare candidate skills with job requirements.
- Generate explainable recruitment insights.
- Provide a simple dashboard for demonstration.
- Maintain human involvement in the final recruitment decision.

---

## ✨ Features

### 1. Candidate Dataset

Candidate information is stored in a CSV file.

The dataset includes:

- Candidate ID
- Name
- Education
- Experience
- Skills
- Projects
- Certifications
- Candidate Summary

### 2. Job Description

The target job requirements are stored in a text file.

The demonstration uses a:

**Junior Data Scientist** position.

### 3. AI Candidate Analysis

The Gemini LLM analyzes the candidate against the job description.

### 4. Match Score

The AI generates an overall match score from:

**0 – 100**

### 5. Skills Analysis

The system identifies:

- Matching skills
- Missing skills

### 6. Strengths and Weaknesses

The AI generates relevant candidate strengths and areas for improvement.

### 7. Recruitment Recommendation

The system provides one of the following recommendations:

- `SHORTLIST`
- `CONSIDER`
- `REJECT`

### 8. Interview Questions

The AI generates three interview questions based on the candidate's profile and job requirements.

### 9. Candidate Ranking

Multiple candidates can be analyzed and ranked according to their generated match scores.

### 10. Streamlit Dashboard

A simple Streamlit interface allows users to select a candidate and generate an AI analysis.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Google Gemini API | Generative AI / LLM |
| google-genai | Gemini Python SDK |
| Pandas | Dataset processing |
| Python-dotenv | Environment variable management |
| Streamlit | Web dashboard |
| CSV | Candidate dataset |
| TXT | Job description |
| Git & GitHub | Version control |

---

## 📂 Project Structure

```text
AI-Recruitment-Assistant/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
│
├── app.py
├── ai_engine.py
├── test_ai.py
├── rank_candidates.py
├── create_dataset.py
│
├── data/
│   ├── candidates.csv
│   ├── job_description.txt
│   └── candidate_results.csv
│
└── venv/
