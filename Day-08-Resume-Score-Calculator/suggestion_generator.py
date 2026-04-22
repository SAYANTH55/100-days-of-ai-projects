def generate_suggestions(missing_skills):
    suggestions = []

    if "AWS" in missing_skills:
        suggestions.append(
            "Add cloud-related projects or AWS certification"
        )

    if "Docker" in missing_skills:
        suggestions.append(
            "Learn Docker and include containerization projects"
        )

    if "Deep Learning" in missing_skills:
        suggestions.append(
            "Add deep learning projects using TensorFlow or PyTorch"
        )

    if not suggestions:
        suggestions.append(
            "Your resume is well aligned with the job description"
        )

    return suggestions