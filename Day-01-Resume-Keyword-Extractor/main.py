import spacy
import PyPDF2
import os

# Load NLP model
nlp = spacy.load("en_core_web_sm")


# Extract text from TXT
def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# Extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text


# Extract keywords using NLP
def extract_keywords(text):
    doc = nlp(text)

    skills = [
        "Python", "Machine Learning", "AI", "NLP",
        "Data Science", "SQL", "Pandas", "NumPy",
        "Scikit-learn", "Git", "GitHub", "Deep Learning"
    ]

    found_skills = []

    for token in doc:
        if token.text in skills:
            found_skills.append(token.text)

    return list(set(found_skills))

# Ask user for file name
file_path = input("Enter file name (sample_resume.txt / sample_resume.pdf): ")


# Check if file exists
if not os.path.exists(file_path):
    print("File not found! Make sure file is in same folder.")
    exit()


# Process file
if file_path.lower().endswith(".pdf"):
    text = extract_text_from_pdf(file_path)
else:
    text = extract_text_from_txt(file_path)


# Extract keywords
keywords = extract_keywords(text)

print("\nExtracted Keywords:\n")

for word in keywords:
    print(word)