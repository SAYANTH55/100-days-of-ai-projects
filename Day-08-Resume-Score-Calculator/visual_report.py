import matplotlib.pyplot as plt

def generate_visual_report(matched, missing, score):
    labels = [
        "Matched Skills",
        "Missing Skills",
        "Resume Score"
    ]

    # Better balanced values
    sizes = [
        len(matched),
        len(missing),
        100 - len(missing)   # instead of raw score
    ]

    plt.figure(figsize=(10, 7))

    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140
    )

    plt.title("Resume ATS Score Report")
    plt.axis("equal")

    plt.show(block=True)