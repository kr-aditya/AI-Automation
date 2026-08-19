# 🤖 AI Career Mentor

An AI-powered career assistant that analyzes a user's resume and generates a personalized career profile, learning roadmap, project recommendations, and interview preparation.

The project combines **LLMs, LangChain, RAG, embeddings, vector databases, structured output, and Streamlit** into one end-to-end application.

---

## 🚀 Features

### Resume Analysis
Upload a PDF resume and extract relevant career information using a RAG pipeline.

The system identifies:

- Candidate summary
- Current/recent role
- Suitable job roles
- Technical skills
- Strengths
- Weaknesses
- Skill gaps
- Learning priorities

### 🎯 Career Analysis

Generates a personalized assessment of the candidate's current career position and job readiness.

### 🗺️ Learning Roadmap

Creates a structured learning roadmap based on the candidate's existing skills and skill gaps.

### 🚀 Project Recommendations

Suggests practical projects that can help the candidate close skill gaps and strengthen their portfolio.

### 🎤 Interview Preparation

Generates interview preparation based on:

- Career analysis
- Skill gaps
- Learning roadmap
- Recommended projects

---

## 🧠 Architecture

```text
                  Resume PDF
                      │
                      ▼
                PDF Loader
                      │
                      ▼
              Document Splitting
                      │
                      ▼
                  Embeddings
                      │
                      ▼
                  ChromaDB
                      │
                      ▼
                 Retriever
                      │
                      ▼
              Resume Context
                      │
                      ▼
              Resume Analysis
                      │
          ┌───────────┼────────────┐
          ▼           ▼            ▼
      Roadmap      Projects     Interview
          │           │            │
          └───────────┼────────────┘
                      ▼
                 Streamlit UI