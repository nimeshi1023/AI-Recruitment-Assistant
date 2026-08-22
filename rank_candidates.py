import pandas as pd
import re

from ai_engine import analyze_candidate


# ============================================================
# LOAD DATA
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
# STORE RESULTS
# ============================================================

results = []


# ============================================================
# ANALYZE ALL CANDIDATES
# ============================================================

for index, candidate in df.iterrows():

    print("\n")
    print("=" * 70)

    print(
        f"Analyzing "
        f"{candidate['candidate_id']} - "
        f"{candidate['name']}"
    )

    print("=" * 70)


    try:

        result = analyze_candidate(
            candidate,
            job_description
        )


        print(result)


        # ----------------------------------------------------
        # Extract Match Score
        # ----------------------------------------------------

        score_match = re.search(
            r"Match Score.*?(\d{1,3})",
            result,
            re.IGNORECASE
        )


        if score_match:

            score = int(
                score_match.group(1)
            )

        else:

            score = 0


        # ----------------------------------------------------
        # Extract Recommendation
        # ----------------------------------------------------

        recommendation = "CONSIDER"

        result_upper = result.upper()


        if "SHORTLIST" in result_upper:

            recommendation = "SHORTLIST"

        elif "REJECT" in result_upper:

            recommendation = "REJECT"


        # ----------------------------------------------------
        # Save result
        # ----------------------------------------------------

        results.append({

            "candidate_id":
                candidate["candidate_id"],

            "name":
                candidate["name"],

            "match_score":
                score,

            "recommendation":
                recommendation,

            "ai_analysis":
                result

        })


    except Exception as e:

        print(
            f"Error analyzing "
            f"{candidate['name']}: {e}"
        )


# ============================================================
# CREATE RESULTS DATAFRAME
# ============================================================

results_df = pd.DataFrame(
    results
)


# ============================================================
# SORT BY SCORE
# ============================================================

results_df = results_df.sort_values(
    by="match_score",
    ascending=False
)


# ============================================================
# ADD RANK
# ============================================================

results_df.insert(
    0,
    "rank",
    range(1, len(results_df) + 1)
)


# ============================================================
# SAVE RESULTS
# ============================================================

results_df.to_csv(
    "data/candidate_results.csv",
    index=False
)


# ============================================================
# DISPLAY FINAL RANKING
# ============================================================

print("\n\n")
print("=" * 70)
print("FINAL CANDIDATE RANKING")
print("=" * 70)

print(
    results_df[
        [
            "rank",
            "candidate_id",
            "name",
            "match_score",
            "recommendation"
        ]
    ].to_string(index=False)
)


print("\n")
print("=" * 70)
print("Results saved to:")
print("data/candidate_results.csv")
print("=" * 70)