import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from scripts.extract_text import extract_all_resumes
from scripts.job_description import load_job_description
from scripts.scorer import tfidf_score, bert_score
from analyzer import extract_keywords_from_text, keyword_match_accuracy, jd_coverage_score

# ✅ Page setup
st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧠")

st.title("📄 AI Resume Analyzer (BERT Powered)")
st.markdown("This tool compares resumes with a job description and ranks them using semantic similarity and keyword matching.")

# ✅ Load JD and extract custom phrases
jd_text = load_job_description()
jd_keywords = extract_keywords_from_text(jd_text)

# ✅ Show JD
st.subheader("📝 Job Description")
st.text_area("Your Job Description", jd_text, height=200, disabled=True)

# ✅ Analyze resumes
resumes = extract_all_resumes("resumes")

if resumes:
    st.subheader("📂 Resume Comparison Table")

    result_data = []
    for filename, content in resumes.items():
        tfidf = tfidf_score(content, jd_text)
        bert = bert_score(content, jd_text)
        coverage = jd_coverage_score(jd_text, content)

        resume_keywords = extract_keywords_from_text(content, jd_keywords)
        accuracy, _, _ = keyword_match_accuracy(jd_keywords, resume_keywords)

        result_data.append({
            "Filename": filename,
            "TF-IDF": round(tfidf, 4),
            "BERT": round(bert, 4),
            "Word Match %": round(coverage, 2),
            "JD Accuracy %": round(accuracy, 2)
        })

    df = pd.DataFrame(result_data)
    df.sort_values("BERT", ascending=False, inplace=True)
    st.dataframe(df, use_container_width=True)
else:
    st.warning("No resumes found in the 'resumes/' folder.")
