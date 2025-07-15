# import re
# from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# from scripts.extract_text import extract_all_resumes, extract_text_from_pdf
# from scripts.job_description import load_job_description
# from scripts.scorer import tfidf_score, bert_score
# from scripts.pdf_to_keywords import process_all_pdfs

# # ✅ Extract keywords from text (JD or resume)
# def extract_keywords_from_text(text):
#     text = text.lower()
#     text = re.sub(r"[^a-z\s]", " ", text)  # remove punctuation
#     words = text.split()
#     keywords = sorted(set([w for w in words if w not in ENGLISH_STOP_WORDS and len(w) > 2]))
#     return keywords

# # ✅ JD Coverage % calculator (word-level overlap)
# def jd_coverage_score(jd_text, resume_text):
#     jd_words = set(jd_text.lower().split())
#     resume_words = set(resume_text.lower().split())
#     matched = jd_words.intersection(resume_words)
#     coverage = len(matched) / len(jd_words) if jd_words else 0
#     return round(coverage * 100, 2)

# # ✅ JD Keyword Match Accuracy
# def keyword_match_accuracy(jd_keywords, resume_keywords):
#     jd_set = set(jd_keywords)
#     resume_set = set(resume_keywords)
#     matched = jd_set.intersection(resume_set)
#     accuracy = len(matched) / len(jd_set) if jd_set else 0
#     return round(accuracy * 100, 2), sorted(matched)

# # ✅ Convert all PDFs to keyword .txt files
# process_all_pdfs("resumes")

# # Preview raw resume PDF text
# resume_text = extract_text_from_pdf("resumes/Tilak-Resume.pdf")
# print("\u2b07\ufe0f Extracted Resume Text (First 1000 characters):\n")
# print(resume_text[:1000])
# print("\n--- End of Preview ---\n")

# # Main resume analysis
# def analyze_resumes(resume_dir="resumes"):
#     jd_text = load_job_description()
#     jd_keywords = extract_keywords_from_text(jd_text)

#     resumes = extract_all_resumes(resume_dir)
#     if not resumes:
#         print("\u26a0\ufe0f No resumes found.")
#         return

#     results = []
#     for filename, content in resumes.items():
#         tfidf = tfidf_score(content, jd_text)
#         bert = bert_score(content, jd_text)
#         coverage = jd_coverage_score(jd_text, content)
#         resume_keywords = content.lower().split()
#         accuracy, matched_keywords = keyword_match_accuracy(jd_keywords, resume_keywords)
#         results.append((filename, tfidf, bert, coverage, accuracy, matched_keywords))

#     results.sort(key=lambda x: x[2], reverse=True)

#     print("\U0001f4c8 Results (sorted by BERT score):\n")
#     print(f"{'Filename':<30} | {'TF-IDF':^8} | {'BERT':^8} | {'Word Match %':^12} | {'JD Accuracy %':^14}")
#     print("-" * 90)
#     for name, tfidf, bert, coverage, accuracy, matched in results:
#         print(f"{name:<30} | {tfidf:^8.4f} | {bert:^8.4f} | {coverage:^12.2f}% | {accuracy:^14.2f}%")
#         # Uncomment to view matched keywords:
#         # print(f"  ✅ Matched JD Keywords: {matched}\n")

# if __name__ == "__main__":
#     analyze_resumes()

#-----------------------------------
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

from scripts.extract_text import extract_all_resumes, extract_text_from_pdf
from scripts.job_description import load_job_description
from scripts.scorer import tfidf_score, bert_score
from scripts.pdf_to_keywords import process_all_pdfs

# ✅ Extract keywords from text (JD or resume) with optional phrase support
def extract_keywords_from_text(text, custom_phrases=None):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)

    words = text.split()
    keywords = sorted(set([w for w in words if w not in ENGLISH_STOP_WORDS and len(w) > 2]))

    if custom_phrases:
        for phrase in custom_phrases:
            phrase_words = phrase.split()
            if all(word in text for word in phrase_words):
                text += f" {phrase}"

    return keywords

# ✅ JD Coverage % calculator (word-level overlap)
def jd_coverage_score(jd_text, resume_text):
    jd_words = set(jd_text.lower().split())
    resume_words = set(resume_text.lower().split())
    matched = jd_words.intersection(resume_words)
    coverage = len(matched) / len(jd_words) if jd_words else 0
    return round(coverage * 100, 2)

# ✅ JD Keyword Match Accuracy
def keyword_match_accuracy(jd_keywords, resume_keywords):
    jd_set = set(jd_keywords)
    resume_set = set(resume_keywords)
    matched = jd_set.intersection(resume_set)
    missing = jd_set - resume_set
    accuracy = len(matched) / len(jd_set) if jd_set else 0
    return round(accuracy * 100, 2), sorted(matched), sorted(missing)

# ✅ Optional: preview & test from command line
def analyze_resumes(resume_dir="resumes"):
    jd_text = load_job_description()
    jd_keywords = jd_keywords = extract_keywords_from_text(jd_text)

    resumes = extract_all_resumes(resume_dir)
    if not resumes:
        print("⚠️ No resumes found.")
        return

    results = []
    for filename, content in resumes.items():
        tfidf = tfidf_score(content, jd_text)
        bert = bert_score(content, jd_text)
        coverage = jd_coverage_score(jd_text, content)
        resume_keywords = extract_keywords_from_text(content, jd_keywords)
        accuracy, matched, missing = keyword_match_accuracy(jd_keywords, resume_keywords)

        results.append((filename, tfidf, bert, coverage, accuracy, matched, missing))

    results.sort(key=lambda x: x[2], reverse=True)

    print("📊 Results (sorted by BERT score):\n")
    print(f"{'Filename':<30} | {'TF-IDF':^8} | {'BERT':^8} | {'Word Match %':^12} | {'JD Accuracy %':^14}")
    print("-" * 90)
    for name, tfidf, bert, coverage, accuracy, matched, missing in results:
        print(f"{name:<30} | {tfidf:^8.4f} | {bert:^8.4f} | {coverage:^12.2f}% | {accuracy:^14.2f}%")

    print(f"  ✅ Matched JD Keywords ({len(matched)}): {matched}")
    print(f"  ❌ Missing JD Keywords ({len(missing)}): {missing}\n")


if __name__ == "__main__":
    process_all_pdfs("resumes")
    analyze_resumes()
