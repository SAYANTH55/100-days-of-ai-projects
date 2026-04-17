def extract_skills(text):

    skills_list = [
        "python", "java", "c++", "machine learning",
        "deep learning", "sql", "data analysis",
        "nlp", "tensorflow", "pandas"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


job_description = input("Enter Job Description: ")

skills = extract_skills(job_description)

print("Skills Found:", ", ".join(skills))