import pandas as pd

from ai_engine import analyze_candidate


# ============================================================
# LOAD CANDIDATE DATASET
# ============================================================

df = pd.read_csv(
    "data/candidates.csv"
)


# ============================================================
# LOAD JOB DESCRIPTION
# ============================================================

with open(
    "data/job_description.txt",
    "r",
    encoding="utf-8"
) as file:

    job_description = file.read()


# ============================================================
# SELECT FIRST CANDIDATE
# ============================================================

candidate = df.iloc[0]


print("=" * 70)
print("AI RECRUITMENT ASSISTANT")
print("=" * 70)

print(
    f"\nAnalyzing Candidate: "
    f"{candidate['name']}"
)

print(
    f"Candidate ID: "
    f"{candidate['candidate_id']}"
)


# ============================================================
# ANALYZE CANDIDATE
# ============================================================

result = analyze_candidate(
    candidate,
    job_description
)


# ============================================================
# DISPLAY RESULT
# ============================================================

print("\n")
print("=" * 70)
print("AI CANDIDATE ANALYSIS")
print("=" * 70)

print(result)

print("\n")
print("=" * 70)
print("Analysis Completed")
print("=" * 70)