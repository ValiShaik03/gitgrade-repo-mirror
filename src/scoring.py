def calculate_score(data):
    breakdown = {}

    breakdown["Documentation"] = 20 if data["readme"] else 0
    breakdown["Commits"] = 20 if data["commits"] >= 10 else 10 if data["commits"] >= 3 else 0
    breakdown["Project Structure"] = 20 if data["files"] >= 5 else 0
    breakdown["Tech Stack Usage"] = 20 if data["language"] else 0
    breakdown["Community Signals"] = 20 if data["stars"] > 0 else 0

    score = sum(breakdown.values())
    return max(score, 15), breakdown


def get_level(score):
    if score >= 80:
        return "Advanced"
    elif score >= 50:
        return "Intermediate"
    else:
        return "Beginner"
