# 🪞 GitGrade – Repository Mirror

GitGrade is an **AI-assisted developer evaluation tool** that analyzes a GitHub repository and converts it into a **recruiter-style score, technical summary, and personalized improvement roadmap**.

This project is inspired by how **modern tech companies use AI + engineering judgement** to evaluate developers beyond traditional coding tests.

---

## 🚀 What GitGrade Does

GitGrade accepts a **public GitHub repository URL** and evaluates it the way a **recruiter or senior engineer** would.

It generates three key outputs:

- 📊 **Repository Score (0–100)**
- 📝 **Recruiter-style Evaluation Summary**
- 🧭 **Personalized Improvement Roadmap**

The goal is to help students understand **how their GitHub actually looks to the industry**.

---

## 🧠 How AI Is Used in This Project

This system uses **AI-assisted reasoning**, not black-box scoring.

### 🔹 AI-style Evaluation Layer
AI-inspired logic is used to:
- Generate **human-like technical summaries**
- Identify **strengths and weaknesses**
- Create a **mentor-style improvement roadmap**

This mirrors how AI tools assist recruiters by **analyzing patterns and providing contextual feedback**, rather than making opaque decisions.

### 🔹 Rule-Based Scoring for Transparency
To ensure fairness and explainability:
- Scoring is **rule-based**
- Each score component is **clearly visible**
- No hidden or unverifiable AI decisions are made

This hybrid approach reflects **real-world AI evaluation systems** where AI supports judgement, not replaces it.

---

## 📐 Evaluation Signals Used

The system analyzes publicly available GitHub signals such as:

- README & documentation quality
- Commit frequency and consistency
- Project structure and organization
- Tech stack usage
- Community indicators (stars)

These signals are commonly used by recruiters and AI-powered hiring tools to assess developer maturity.

---

## 📊 Output Breakdown

For every repository, GitGrade provides:

- **Overall Score** (0–100)
- **Skill Level Badge** (Beginner / Intermediate / Advanced)
- **Score Breakdown** across multiple dimensions
- **Recruiter-style written summary**
- **Strengths & areas for improvement**
- **Actionable roadmap** to improve the repository

---

## 🧪 Why This Is Industry-Relevant

- Reflects how **AI-assisted hiring tools work today**
- Prioritizes **explainability and engineering judgement**
- Evaluates **real developer output**, not theoretical answers
- Encourages **continuous improvement**, not just scoring

This project demonstrates how developers can **use AI thoughtfully** to build better evaluation systems.

---

## ⚠️ Current Limitations

- Uses only public GitHub data
- No deep static code analysis yet
- No PR-level or issue-level analysis

These are intentional trade-offs to keep the system **clear, fast, and explainable**.

---

## 🔮 Future Improvements

- Deep static code analysis using AST parsing
- PR and issue activity evaluation
- LLM-powered natural language insights
- Support for profile-level analysis

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
