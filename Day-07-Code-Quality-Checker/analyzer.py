import ast

def check_syntax(file_path):
    try:
        with open(file_path, "r") as file:
            code = file.read()
            ast.parse(code)
        return "✅ No Syntax Errors Found"
    except SyntaxError as e:
        return f"❌ Syntax Error: {e}"