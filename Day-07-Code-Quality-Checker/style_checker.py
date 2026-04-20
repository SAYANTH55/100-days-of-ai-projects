def check_style(file_path):
    issues = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines, start=1):
        if len(line) > 79:
            issues.append(f"Line {line_number}: Too long (>79 characters)")

        if "=" in line and " = " not in line and "==" not in line:
            issues.append(f"Line {line_number}: Missing spaces around '='")

    if not issues:
        return ["✅ No Style Issues Found"]

    return issues