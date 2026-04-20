def generate_score(style_issues, syntax_result, complexity_issues):
    score = 100

    if "Syntax Error" in syntax_result:
        score -= 30

    score -= len(style_issues) * 5
    score -= len(complexity_issues) * 10

    if score < 0:
        score = 0

    return score