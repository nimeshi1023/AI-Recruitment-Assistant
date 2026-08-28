import streamlit as st
import pandas as pd

from ai_engine import analyze_candidate


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Recruitment Assistant",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title(
    "🤖 AI Recruitment Assistant"
)

st.write(
    "Generative AI powered candidate screening "
    "and job matching system"
)


st.divider()


# ============================================================
# LOAD CANDIDATE DATASET
# ============================================================

try:

    df = pd.read_csv(
        "data/candidates.csv"
    )

except FileNotFoundError:

    st.error(
        "candidates.csv not found. "
        "Please run create_dataset.py first."
    )

    st.stop()


# ============================================================
# LOAD JOB DESCRIPTION
# ============================================================

try:

    with open(
        "data/job_description.txt",
        "r",
        encoding="utf-8"
    ) as file:

        job_description = file.read()

except FileNotFoundError:

    st.error(
        "job_description.txt not found."
    )

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header(
    "Candidate Selection"
)


selected_candidate = st.sidebar.selectbox(
    "Select Candidate",
    df["name"].tolist()
)


# ============================================================
# GET SELECTED CANDIDATE
# ============================================================

candidate = df[
    df["name"] == selected_candidate
].iloc[0]


# ============================================================
# CANDIDATE INFORMATION
# ============================================================

st.header(
    "👤 Candidate Information"
)


col1, col2 = st.columns(2)


with col1:

    st.write(
        "**Candidate ID:**",
        candidate["candidate_id"]
    )

    st.write(
        "**Name:**",
        candidate["name"]
    )

    st.write(
        "**Education:**",
        candidate["education"]
    )

    st.write(
        "**Experience:**",
        f"{candidate['experience_years']} years"
    )


with col2:

    st.write(
        "**Skills:**",
        candidate["skills"]
    )

    st.write(
        "**Projects:**",
        candidate["projects"]
    )

    st.write(
        "**Certifications:**",
        candidate["certifications"]
    )


st.divider()



# JOB DESCRIPTION

st.header(
    "💼 Job Description"
)


st.text_area(
    "Job Description",
    job_description,
    height=250,
    disabled=True
)


st.divider()



# ANALYZE BUTTON


if st.button(
    "🔍 Analyze Candidate",
    type="primary",
    use_container_width=True
):

    with st.spinner(
        "🤖 AI is analyzing the candidate..."
    ):

        try:

            result = analyze_candidate(
                candidate,
                job_description
            )


            st.success(
                "Candidate analysis completed!"
            )


            # ------------------------------------------------
            # DISPLAY RESULT
            # ------------------------------------------------

            st.header(
                "🤖 AI Candidate Analysis"
            )


            st.markdown(
                result
            )


        except Exception as e:

            st.error(
                f"An error occurred: {e}"
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI Recruitment Assistant | "
    "Generative AI Application"
)