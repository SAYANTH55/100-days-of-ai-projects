def match_skills(resume_skills, jd_skills):
    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills.difference(resume_skills)

    return matched, missing