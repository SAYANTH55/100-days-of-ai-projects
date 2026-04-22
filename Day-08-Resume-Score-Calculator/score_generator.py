def generate_score(matched, jd_skills):
    if len(jd_skills) == 0:
        return 0

    score = (len(matched) / len(jd_skills)) * 100
    return round(score, 2)