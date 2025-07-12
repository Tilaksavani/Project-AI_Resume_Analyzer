import os
import re
import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def convert_text_to_keywords(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)  # Remove everything except letters
    words = text.split()
    keywords = sorted(set(words))  # Remove duplicates and sort alphabetically
    return keywords

def save_keywords_to_file(keywords, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(keywords))

def process_all_pdfs(folder_path="resumes"):
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]
    if not pdf_files:
        print(f"⚠️ No PDF files found in: {folder_path}")
        return

    for file in pdf_files:
        pdf_path = os.path.join(folder_path, file)
        txt_filename = os.path.splitext(file)[0] + "-keywords.txt"
        txt_path = os.path.join(folder_path, txt_filename)

        try:
            print(f"📄 Extracting from: {file}")
            text = extract_text_from_pdf(pdf_path)
            if not text.strip():
                print(f"⚠️ Empty text from {file}")
                continue
            keywords = convert_text_to_keywords(text)
            save_keywords_to_file(keywords, txt_path)
            print(f"✅ Saved keywords to: {txt_filename} ({len(keywords)} keywords)")
        except Exception as e:
            print(f"❌ Error processing {file}: {e}")

if __name__ == "__main__":
    process_all_pdfs("resumes")
