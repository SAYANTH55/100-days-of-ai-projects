import matplotlib.pyplot as plt

def generate_visual_report(style_issues, complexity_issues, final_score):
    labels = ["Style Issues", "Complexity Issues", "Code Score"]
    sizes = [
        len(style_issues),
        len(complexity_issues),
        final_score
    ]

    # Better layout
    plt.figure(figsize=(10, 7))  # bigger canvas

    wedges, texts, autotexts = plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140,
        radius=0.8,              # 👈 reduces zoom
        pctdistance=0.75,        # 👈 moves % inside nicely
        labeldistance=1.1        # 👈 pushes labels outward
    )

    # Title
    plt.title("Python Code Quality Report", fontsize=14)

    # Legend outside (clean look)
    plt.legend(
        wedges,
        labels,
        title="Metrics",
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )

    plt.tight_layout()  # prevents cutting
    plt.show()