from analyzer import check_syntax
from style_checker import check_style
from complexity_checker import check_complexity
from score_generator import generate_score
from visual_report import generate_visual_report

file_path = "sample_code.py"

print("\n🚀 Advanced Python Code Quality Checker\n")

# Syntax Check
syntax_result = check_syntax(file_path)
print("Syntax Analysis:")
print(syntax_result)

# Style Check
print("\nStyle Analysis:")
style_issues = check_style(file_path)

for issue in style_issues:
    print(issue)

# Complexity Check
print("\nComplexity Analysis:")
complexity_issues = check_complexity(file_path)

for issue in complexity_issues:
    print(issue)

# Final Score
final_score = generate_score(
    style_issues,
    syntax_result,
    complexity_issues
)

print(f"\n⭐ Final Code Quality Score: {final_score}/100")

# Visual Report
generate_visual_report(
    style_issues,
    complexity_issues,
    final_score
)