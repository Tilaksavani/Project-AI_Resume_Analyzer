import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from scripts.extract_text import extract_all_resumes
from scripts.job_description import load_job_description
from scripts.scorer import bert_score

st.set_page_config(page_title="AI Resume Analyzer", page_icon="\U0001F9E0")

st.title("\U0001F4C4 AI Resume Analyzer (BERT Powered)")
st.markdown("This tool compares resumes with a job description and ranks them using semantic similarity.")

jd = load_job_description()

st.subheader("\U0001F4DD Job Description")
st.text_area("Your Job Description", jd, height=200, disabled=True)

resumes = extract_all_resumes("resumes")

if resumes:
    st.subheader("\U0001F4C2 Resume Scores")

    result_data = []
    for filename, content in resumes.items():
        score = bert_score(content, jd)
        result_data.append((filename, score))

    result_data.sort(key=lambda x: x[1], reverse=True)

    for name, score in result_data:
        st.markdown(f"- **{name}** → Score: `{score}`")
else:
    st.warning("No resumes found in the 'resumes/' folder.")