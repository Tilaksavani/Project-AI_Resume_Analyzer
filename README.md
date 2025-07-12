# 🤖 AI Resume Analyzer

This project analyzes resumes against a job description to evaluate their relevance using:

- ✅ **BERT** (semantic similarity)
- ✅ **TF-IDF** (textual similarity)
- ✅ **JD Coverage** (word-level match)
- ✅ **JD Keyword Accuracy** (keyword presence & missing skills)

It helps job seekers improve their resumes and recruiters prioritize candidates with the most aligned skills.

---

## 📁 Project Structure

AI-Resume-Analyzer/
├── app/
| ├── app.py
├── scripts/
| ├── __init__.py
│ ├── extract_text.py # Resume file loader
│ ├── pdf_to_keywords.py # Converts PDF to cleaned keyword .txt
│ ├── job_description.py # Loads job_description.txt
│ ├── scorer.py # TF-IDF and BERT scoring
├── resumes/ # Place your PDF resumes here
│ ├── Tilak-Resume.pdf
│ ├── Resume1.pdf
│ └── ...
├── job_description.txt # Your target job description
├── analyzer.py # ✅ Main analysis script
├── requirements.txt # Dependencies
└── README.md

---

## 🔧 How It Works

### ✅ Inputs:

- `resumes/*.pdf` → Automatically converted into keywords
- `job_description.txt` → Extracted into keywords dynamically

### ✅ Output:

- Ranking of resumes based on BERT, TF-IDF, and keyword match
- Lists of:
  - ✅ Matched JD skills
  - ❌ Missing JD skills
- Resume scoring printed in table format

---

## 🚀 Run the Analyzer

### 1. 📦 Install Dependencies

```bash
pip install -r requirements.txt## 💡 Use Cases
```

### 2. 📂 Add Files

- Put all your resume PDFs into the resumes/ folder.
- Write your job description in job_description.txt.

### 3. ▶️ Run the script

```bash
python analyzer.py
```

---

## 📊 Sample Output

📈 Results (sorted by BERT score):

## Filename | TF-IDF | BERT | Word Match % | JD Accuracy %

Tilak-Resume-keywords.txt | 0.8652 | 0.9211 | 72.00% | 88.89%
✅ Matched JD Keywords (16): ['python', 'tensorflow', 'cnn', 'keras', ...]
❌ Missing JD Keywords (2): ['netcdf', 'huggingface']

---

## 💡 Use Cases

- 🧑‍🎓 **Students** preparing for internship/job fairs
- 🧠 **Candidates** checking resume alignment
- 🧑‍💼 **Recruiters** shortlisting relevant profiles
- 🎯 **Resume optimization** with measurable scores

---

## 🧠 Features

| Feature             | Description                                         |
|---------------------|-----------------------------------------------------|
| **BERT Score**      | Semantic similarity using sentence embeddings       |
| **TF-IDF Score**    | Textual similarity based on frequency               |
| **JD Coverage %**   | Word overlap between JD and resume                  |
| **JD Accuracy %**   | Skill keyword match rate                            |
| **Missing Keywords**| Clear output of what to add in resume               |
| **Keyword Extraction** | Cleaned, stopword-removed skill tokens           |

---

## 🧰 Tech Stack

- Python
- pdfplumber
- scikit-learn
- Sentence Transformers (BERT)
- matplotlib *(optional for future visuals)*

---

## ✅ Example Resume Keywords Extraction

```txt
python
tensorflow
keras
cnn
pandas
netcdf
drowsiness
...

```
---

## 🙋‍♂️ Author

**Tilak Savani**  
Master’s in Computer Science, University of Georgia  
Domain: Artificial Intelligence & Machine Learning  

---

## ⭐ Credits

- [Hugging Face Transformers](https://huggingface.co/)
- [Scikit-learn Team](https://scikit-learn.org/)
- [UCI ML Datasets](https://archive.ics.uci.edu/ml/index.php)
- [Streamlit Community](https://streamlit.io/)

---

## 📄 License

This project is open-source and available under the **MIT License**.
