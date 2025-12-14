def generate_summary(data, score):
    summary = []

    summary.append(
        f"This repository scores {score}/100 based on documentation quality, "
        "commit activity, project structure, and overall GitHub usage."
    )

    if data["readme"]:
        summary.append(
            "The presence of a README suggests an effort toward documentation and usability."
        )
    else:
        summary.append(
            "The lack of a comprehensive README reduces clarity for recruiters and collaborators."
        )

    if data["commits"] >= 10:
        summary.append(
            "The commit history reflects consistent development and good version control practices."
        )
    elif data["commits"] >= 3:
        summary.append(
            "There is some commit activity, though more frequent commits would improve development traceability."
        )
    else:
        summary.append(
            "Minimal commit activity suggests limited iteration or incomplete development."
        )

    if data["files"] >= 5:
        summary.append(
            "The repository shows a reasonably organized structure, aiding readability and scalability."
        )
    else:
        summary.append(
            "The project structure is minimal and could benefit from clearer separation of concerns."
        )

    summary.append(
        "Overall, this repository demonstrates foundational engineering skills. "
        "With stronger documentation, testing, and development consistency, "
        "it can better reflect industry-ready practices."
    )

    return " ".join(summary)


def generate_strengths_weaknesses(data):
    strengths = []
    weaknesses = []

    if data["readme"]:
        strengths.append("Includes basic project documentation")
    else:
        weaknesses.append("Missing or weak README documentation")

    if data["commits"] >= 10:
        strengths.append("Consistent commit history")
    else:
        weaknesses.append("Inconsistent or limited commit activity")

    if data["files"] >= 5:
        strengths.append("Reasonable project structure")
    else:
        weaknesses.append("Minimal or flat project structure")

    return strengths, weaknesses


def generate_roadmap(data):
    roadmap = []

    if not data["readme"]:
        roadmap.append("Add a detailed README with setup and usage instructions")

    if data["commits"] < 10:
        roadmap.append("Commit more frequently with clear, meaningful messages")

    roadmap.extend([
        "Add unit or integration tests",
        "Improve folder structure for scalability",
        "Set up CI/CD using GitHub Actions"
    ])

    return roadmap[:5]
