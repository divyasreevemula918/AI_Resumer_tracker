# 🤖 AI Resume Tracker

An AI-powered Resume Tracking and ATS Analysis application built using Python, Streamlit, and Generative AI.

This project helps users analyze resumes against job descriptions by calculating ATS match scores, identifying missing skills, and generating AI-powered suggestions for resume improvement.

---

# 🚀 Features

- 📄 Upload Resume (PDF)
- 💼 Paste Job Description
- 🎯 ATS Match Score Calculation
- 🤖 AI-Powered Resume Analysis
- ✅ Skill Matching
- ❌ Missing Skill Detection
- 💡 Resume Improvement Suggestions
- 🧠 NLP-based Resume Processing
- 🎨 Interactive Streamlit UI

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Generative AI
- Google Gemini API / LLM
- NLP
- PDF Processing
- PyPDF2
- FAISS (if used)
- LangChain (if used)
- JSON

---

# 📂 Project Structure

```bash
AI_Resumer_tracker/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
├── data/
├── uploads/
└── venv/
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/divyasreevemula918/AI_Resumer_tracker.git

cd AI_Resumer_tracker
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure API Key

Create a `.env` file or configure secrets.

Example:

```env
GOOGLE_API_KEY=your_api_key
```

or configure using:

```python
from google.colab import userdata
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📄 How It Works

```text
Upload Resume
       ↓
Extract Resume Text
       ↓
Compare with Job Description
       ↓
AI/NLP Analysis
       ↓
Generate ATS Score & Suggestions
```

---

# 💡 Features Explained

## 🎯 ATS Score Analysis

Calculates how well the resume matches the provided job description.

---

## ✅ Skill Matching

Identifies skills present in the resume.

Example:
- Python
- AWS
- Machine Learning
- SQL

---

## ❌ Missing Skills Detection

Detects important missing keywords from the job description.

Example:
- Docker
- Kubernetes
- CI/CD

---

## 🤖 AI Suggestions

Generates intelligent recommendations to improve resume quality.

Example:
- Add measurable achievements
- Improve technical summary
- Include relevant certifications

---

# 📸 Example Output

```text
ATS Match Score: 85%

Matched Skills:
✔ Python
✔ AWS
✔ Machine Learning

Missing Skills:
❌ Docker
❌ Kubernetes

Suggestions:
• Add cloud deployment projects
• Include certifications
• Improve resume summary
```

---

# 🧠 Learning Outcomes

Through this project, I learned:

- Resume Parsing
- NLP Concepts
- Prompt Engineering
- Streamlit Application Development
- LLM Integration
- AI-based Text Analysis
- PDF Text Extraction
- Generative AI Workflows

---

# 🔥 Future Improvements

- 📄 DOCX Resume Support
- 🌐 Multi-language Resume Analysis
- 📊 Resume Analytics Dashboard
- 🧠 RAG-based Resume Assistant
- ☁️ Cloud Deployment
- 🔍 Semantic Skill Matching
- 📥 Resume Download Feature

---

# 🌍 Deployment

You can deploy this project using:
https://airesumertracker-2qngokdwvvjkfrl8dsirhx.streamlit.app/
---
# output
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ba59e2cb-38e4-4662-ae1d-a682627bd6b5" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f75d3cf8-67e5-4fb9-b93b-ed2df77127ac" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9197f2b3-7ff1-48a4-9cc5-2fc4018f2756" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3b9dc870-04be-4184-9420-9d6b3d65f40d" />



# 📌 Sample Use Case

A student uploads their resume and pastes a Software Engineer job description.

The system:
- analyzes resume content
- checks ATS compatibility
- identifies missing keywords
- provides AI-generated suggestions

---

# 🙌 Acknowledgements

- Streamlit
- Google Gemini API
- Python Community
- LangChain
- FAISS

---

# 👩‍💻 Author

Divya Sree

GitHub:
https://github.com/divyasreevemula918

---
