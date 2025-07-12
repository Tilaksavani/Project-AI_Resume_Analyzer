import os
from PyPDF2 import PdfReader
import pdfplumber

# PdfReader

# def extract_text_from_pdf(file_path):
#     text = ""
#     try:
#         with open(file_path, "rb") as f:
#             reader = PdfReader(f)
#             for page in reader.pages:
#                 text += page.extract_text() or ""
#     except Exception as e:
#         print(f"Error reading {file_path}: {e}")
#     return text

# pdfplumber
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# // direct from pdf
# def extract_all_resumes(resume_folder):
    # resumes = {}
    # for file in os.listdir(resume_folder):
    #     if file.endswith(".txt"):
    #         path = os.path.join(resume_folder, file)
    #         resumes[file] = extract_text_from_pdf(path)
    # return resumes

# // from text
def extract_all_resumes(resume_folder):
    resumes = {}
    for file in os.listdir(resume_folder):
        if file.endswith(".txt"):
            path = os.path.join(resume_folder, file)
            with open(path, "r", encoding="utf-8") as f:
                resumes[file] = f.read()
    return resumes

