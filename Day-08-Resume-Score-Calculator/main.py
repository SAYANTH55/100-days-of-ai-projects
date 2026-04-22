from resume_reader import read_resume
from jd_reader import read_jd
from skill_matcher import match_skills
from score_generator import generate_score
from suggestion_generator import generate_suggestions
from visual_report import generate_visual_report

resume_file = "sample_resume.txt"
jd_file = "sample_jd.txt"

print("\n🚀 Advanced Resume Score Calculator\n")

# Read files
resume_skills = read_resume(resume_file)
jd_skills = read_jd(jd_file)

# Match skills
matched, missing = match_skills(resume_skills, jd_skills)

# Generate score
score = generate_score(matched, jd_skills)

# Suggestions
suggestions = generate_suggestions(missing)

print("Matched Skills:")
for skill in matched:
    print(f"✔ {skill}")

print("\nMissing Skills:")
for skill in missing:
    print(f"✘ {skill}")

print(f"\n⭐ Resume Match Score: {score}%")

# ATS Friendly Feedback
if score >= 80:
    print("ATS Score: Excellent ✅")
elif score >= 60:
    print("ATS Score: Good 👍")
else:
    print("ATS Score: Needs Improvement ⚠")

print("\nSuggestions to Improve Resume:")
for suggestion in suggestions:
    print(f"• {suggestion}")

# Visual Report
generate_visual_report(
    matched,
    missing,
    score
)