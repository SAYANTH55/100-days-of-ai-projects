import ast

def check_complexity(file_path):
    issues = []

    with open(file_path, "r") as file:
        code = file.read()

    tree = ast.parse(code)

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if len(node.body) > 5:
                issues.append(
                    f"Function '{node.name}' is too large and may be hard to maintain"
                )

        if isinstance(node, ast.For):
            nested_loops = sum(
                isinstance(child, ast.For)
                for child in ast.walk(node)
            )

            if nested_loops > 1:
                issues.append(
                    "Nested loops detected — may increase time complexity"
                )

    if not issues:
        return ["✅ No Complexity Issues Found"]

    return issues