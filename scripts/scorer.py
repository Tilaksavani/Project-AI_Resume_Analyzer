
# ---------- TF-IDF ----------
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tfidf_score(resume_text, jd_text):
    """
    Compute cosine similarity between resume and job description using TF-IDF.
    Returns a score between 0 and 1.
    """
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score, 4)


# ---------- BERT ----------
from sentence_transformers import SentenceTransformer, util

# Load pre-trained BERT model once
bert_model = SentenceTransformer("all-MiniLM-L6-v2")

def bert_score(resume_text, jd_text):
    """
    Compute semantic similarity using BERT sentence embeddings.
    Returns a score between 0 and 1.
    """
    embeddings = bert_model.encode([resume_text, jd_text], convert_to_tensor=True)
    score = util.pytorch_cos_sim(embeddings[0], embeddings[1])
    return round(float(score), 4)
