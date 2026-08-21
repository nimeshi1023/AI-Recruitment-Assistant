import pandas as pd
import os

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Candidate dataset
candidates = [
    {
        "candidate_id": "C001",
        "name": "Kasun Perera",
        "education": "BSc in Information Technology",
        "experience_years": 1,
        "skills": "Python, SQL, Pandas, NumPy, Machine Learning, TensorFlow",
        "projects": "Customer Churn Prediction, Sales Forecasting",
        "certifications": "Google Data Analytics Certificate",
        "summary": "Junior data science candidate with experience in Python and machine learning."
    },

    {
        "candidate_id": "C002",
        "name": "Nimal Fernando",
        "education": "BSc in Computer Science",
        "experience_years": 2,
        "skills": "Python, Java, SQL, Power BI, Excel, Machine Learning",
        "projects": "Sales Dashboard, Customer Segmentation",
        "certifications": "Microsoft Power BI Certification",
        "summary": "Data analyst with experience in business intelligence and machine learning."
    },

    {
        "candidate_id": "C003",
        "name": "Amaya Silva",
        "education": "BSc in Data Science",
        "experience_years": 1,
        "skills": "Python, R, SQL, Pandas, NumPy, Scikit-learn, Tableau",
        "projects": "House Price Prediction, Customer Segmentation",
        "certifications": "IBM Data Science Certificate",
        "summary": "Data science graduate with strong statistical and machine learning skills."
    },

    {
        "candidate_id": "C004",
        "name": "Sahan Wijesinghe",
        "education": "BSc in Software Engineering",
        "experience_years": 3,
        "skills": "Java, Spring Boot, React, MySQL, MongoDB, Docker",
        "projects": "E-commerce Platform, Employee Management System",
        "certifications": "AWS Cloud Practitioner",
        "summary": "Software engineer with strong backend and cloud development experience."
    },

    {
        "candidate_id": "C005",
        "name": "Dilki Jayawardena",
        "education": "BSc in Information Technology",
        "experience_years": 0,
        "skills": "Python, SQL, Excel, Power BI, Pandas",
        "projects": "Sales Analytics Dashboard, Customer Data Analysis",
        "certifications": "Microsoft Power BI Certification",
        "summary": "Entry-level candidate interested in data analytics and business intelligence."
    },

    {
        "candidate_id": "C006",
        "name": "Ravindu Perera",
        "education": "BSc in Artificial Intelligence",
        "experience_years": 2,
        "skills": "Python, TensorFlow, PyTorch, Machine Learning, Deep Learning, SQL",
        "projects": "Image Classification, Disease Detection System",
        "certifications": "Deep Learning Specialization",
        "summary": "AI engineer with practical deep learning and computer vision experience."
    },

    {
        "candidate_id": "C007",
        "name": "Tharushi Fernando",
        "education": "BSc in Data Science",
        "experience_years": 1,
        "skills": "Python, SQL, R, Statistics, Machine Learning, Power BI",
        "projects": "Sales Prediction, Customer Churn Analysis",
        "certifications": "Data Science Professional Certificate",
        "summary": "Data science graduate with experience in statistical analysis and visualization."
    },

    {
        "candidate_id": "C008",
        "name": "Chamod Silva",
        "education": "BSc in Information Systems",
        "experience_years": 2,
        "skills": "SQL, Power BI, Excel, Tableau, Python",
        "projects": "Business Intelligence Dashboard, Sales Analysis",
        "certifications": "Microsoft Power BI Certification",
        "summary": "Business intelligence analyst experienced in dashboards and data reporting."
    },

    {
        "candidate_id": "C009",
        "name": "Hiruni Perera",
        "education": "BSc in Computer Science",
        "experience_years": 1,
        "skills": "Python, SQL, Pandas, Scikit-learn, NLP, Machine Learning",
        "projects": "Sentiment Analysis, Recommendation System",
        "certifications": "Machine Learning Certificate",
        "summary": "Machine learning candidate with experience in NLP and recommendation systems."
    },

    {
        "candidate_id": "C010",
        "name": "Pasindu Fernando",
        "education": "BSc in Software Engineering",
        "experience_years": 4,
        "skills": "Java, Python, SQL, AWS, Docker, Kubernetes, Git",
        "projects": "Cloud Application, Microservices Platform",
        "certifications": "AWS Solutions Architect",
        "summary": "Experienced software engineer with strong cloud and DevOps skills."
    }
]

# Convert to DataFrame
df = pd.DataFrame(candidates)

# Save CSV
file_path = "data/candidates.csv"
df.to_csv(file_path, index=False)

print("Candidate dataset created successfully!")
print(f"File saved at: {file_path}")
print(f"Number of candidates: {len(df)}")

print("\nDataset preview:")
print(df.head())