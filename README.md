# 🪞 GitGrade – Repository Mirror

**GitGrade** is an **AI-assisted developer evaluation tool** that analyzes a GitHub repository and converts it into a **recruiter-style score, detailed technical summary, and personalized improvement roadmap**.

This project is inspired by how **modern tech companies evaluate developers using AI + engineering judgement**, not just coding tests.

---

## 🚀 Live Demo

👉 **Streamlit App:**  
https://gitgrade-repo-mirror.streamlit.app

---

## 🎯 Problem Statement

Students and early-career developers often maintain GitHub repositories, but they rarely know:

- How their repository looks to a recruiter
- What signals indicate strong engineering practices
- What exactly to improve to become industry-ready

**GitGrade acts as a “Repository Mirror”**, reflecting the real strengths, weaknesses, and next steps of a GitHub project.

---

## 🧠 What GitGrade Does

GitGrade accepts a **public GitHub repository URL** and produces three key outputs:

- 📊 **Repository Score (0–100)**
- 📝 **Recruiter-style Evaluation Summary**
- 🧭 **Personalized Improvement Roadmap**

The feedback is designed to feel like guidance from a **senior engineer or hiring reviewer**.

---

## 🤖 How AI Is Used in This Project

This system uses **AI-assisted reasoning**, not black-box decision making.

### 🔹 AI-Style Reasoning Layer
AI-inspired logic is used to:
- Generate **human-like technical summaries**
- Identify **strengths and improvement areas**
- Create a **mentor-style roadmap**

This mirrors how AI tools assist recruiters by **analyzing patterns and producing contextual insights**, rather than blindly scoring candidates.

### 🔹 Rule-Based Scoring for Transparency
To ensure explainability and fairness:
- Scoring is **rule-based**
- Every score has a **clear reason**
- No hidden or opaque AI decisions are made

This hybrid approach reflects **real-world AI evaluation systems**, where AI supports judgement instead of replacing it.

---

## 📐 Evaluation Signals Used

The system analyzes publicly available GitHub signals, including:

- README & documentation presence
- Commit frequency and consistency
- Project structure and file organization
- Tech stack usage
- Community indicators (stars)

These are the same signals commonly used by recruiters and AI-assisted hiring tools.

---

## 📊 Output Breakdown

For each repository, GitGrade provides:

- **Overall Score (0–100)**
- **Skill Level Badge** (Beginner / Intermediate / Advanced)
- **Score Breakdown** across evaluation dimensions
- **Recruiter-style written summary**
- **Strengths and areas to improve**
- **Actionable improvement roadmap**

---

## 🧪 Why This Is Industry-Relevant

- Reflects **real AI-assisted hiring workflows**
- Prioritizes **explainability and reasoning**
- Evaluates **real developer output**, not theoretical answers
- Encourages **continuous improvement**, not just ranking

This project demonstrates how developers can **use AI thoughtfully and responsibly**.

---

## 🔐 GitHub API & Rate-Limit Handling

To ensure stability in production environments (e.g., Streamlit Cloud), the app uses **authenticated GitHub API requests**.

- A **GitHub Personal Access Token** is securely stored using **Streamlit Secrets**
- This avoids API rate-limit issues common with unauthenticated requests
- No tokens or credentials are hard-coded or committed to the repository

This mirrors **production-grade engineering practices**.

---

## ⚠️ Current Limitations

- Uses only public GitHub data
- No deep static code analysis yet
- No PR-level or issue-level evaluation

These are intentional trade-offs to keep the system **fast, clear, and explainable**.

---

## 🔮 Future Improvements

- Deep static code analysis using AST parsing
- Pull request and issue activity analysis
- LLM-powered natural language insights
- Profile-level developer evaluation

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
