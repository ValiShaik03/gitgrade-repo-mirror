import streamlit as st
from src.github_client import analyze_repo
from src.scoring import calculate_score, get_level
from src.ai import (
    generate_summary,
    generate_roadmap,
    generate_strengths_weaknesses
)

st.set_page_config(
    page_title="GitGrade – Repository Mirror",
    layout="centered"
)

st.title("🪞 GitGrade – Repository Mirror")
st.caption("Evaluate your GitHub repository like a recruiter")

repo_url = st.text_input(
    "🔗 Enter a public GitHub repository URL",
    placeholder="https://github.com/username/repository"
)

if st.button("Analyze Repository"):

    if not repo_url:
        st.warning("Please enter a GitHub repository URL.")
        st.stop()

    # Validate repo URL (not profile)
    if repo_url.rstrip("/").count("/") < 4:
        st.error("❌ Please enter a valid GitHub REPOSITORY URL.")
        st.info("Example: https://github.com/username/repository")
        st.stop()

    try:
        with st.spinner("Analyzing repository..."):
            repo_data = analyze_repo(repo_url)
            score, breakdown = calculate_score(repo_data)
            level = get_level(score)
            summary = generate_summary(repo_data, score)
            strengths, weaknesses = generate_strengths_weaknesses(repo_data)
            roadmap = generate_roadmap(repo_data)

        st.success("Analysis Complete 🎉")

        st.metric("Repository Score", f"{score} / 100")
        st.success(f"Skill Level: **{level} Developer**")

        st.subheader("📊 Score Breakdown")
        for k, v in breakdown.items():
            st.write(f"{k}: {v} / 20")

        st.subheader("📝 Recruiter-Style Evaluation Summary")
        st.write(summary)

        st.subheader("✅ Strengths")
        for s in strengths:
            st.write(f"• {s}")

        st.subheader("⚠️ Areas to Improve")
        for w in weaknesses:
            st.write(f"• {w}")

        st.subheader("🧭 Personalized Roadmap")
        for step in roadmap:
            st.write(f"• {step}")

    except Exception:
        st.error("❌ Unable to analyze repository.")
        st.info(
            "Please ensure:\n"
            "• The repository exists\n"
            "• It is public\n"
            "• The URL is correct\n\n"
            "Example:\n"
            "https://github.com/username/repository"
        )
